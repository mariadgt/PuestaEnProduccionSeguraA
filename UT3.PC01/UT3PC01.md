# Seguridad y desplegado de aplicaciones con Docker.

UT3.PC01.

## Docker-Bench.

Herramienta de seguridad que verifica la configuración de un host Docker contra un conjunto de prácticas recomendadas de seguridad. Verifica aspectos como la configuración de seguridad de la API Docker, la configuración de seguridad de los contenedores y la configuración de seguridad de la infraestructura subyacente. Proporciona recomendaciones para corregir cualquier problema de seguridad encontrado.

## Pruebas con Docker-Bench.

Comenzamos clonando el repositorio e iniciando la prueba:

![1.JPG](https://github.com/mariadgt/PuestaEnProduccionSeguraA/UT3.PC01/img/1.jpg)

Los “WARN” que nos aparecen son debido a:

- ***1.1.1 - Ensure a separate partition for containers has been created (Automated)***
    
    Docker depende de la carpeta `/var/lib/docker` para almacenar todos los archivos, esta carpeta podría llenarse rápidamente lo que provoca que ni Docker ni el host funcionen. 
    
    Solución:
    
    Para en instalaciones nuevas: creamos una partición separada para el `/var/lib/docker` punto de montaje.
    
    Para instalaciones que ya estaban: usamos el LVM (Administrador de volúmenes lógicos) para crear una nueva partición.
    
- ***1.1.3 - Ensure auditing is configured for the Docker daemon (Automated)***
    
    Nos está diciendo que debido a que el demonio Docker se ejecuta con privilegios de root necesitamos auditarlo para tenerlo bajo control.
    
    Solución:
    
    Debemos agregar una regla en el archivo `/etc/audit/audit.rules` :
    
    ```bash
    -w /usr/bin/dockerd -k docker
    ```
    
    Luego reiniciamos auditd y ya estaría. (`service auditd restart`).
    

## Auditd.

Es un sistema de auditoría que permite monitorear y registrar eventos de seguridad en un SO, estos registros pueden ser analizados para detectar posibles amenazas y tomar medidas para mejorar el sistema.

Para instalarlo sólo ejecutaremos este comando:

```bash
sudo apt install auditd
```

Nos metemos en el fichero `/etc/audit/rules.d/audit.rules` y añadimos las siguientes líneas:

```bash
-w /usr/bin/docker -p wa
-w /var/lib/docker -p wa
-w /etc/docker -p wa
-w /lib/systemd/system/docker.service -p wa 
-w /lib/systemd/system/docker.socket -p wa 
-w /etc/default/docker -p wa
-w /etc/docker/daemon.json -p wa
-w /usr/bin/docker-containerd -p wa
-w /usr/bin/docker-runc -p wa
```

![2.JPG](https://github.com/mariadgt/PuestaEnProduccionSeguraA/UT3.PC01/img/2.jpg)

> Estas líneas solucionarían el último warnig los “Warn” que nos aparecían al ejecutar el Docker-bench.
> 

Reiniciamos el servicio y ya estaríamos auditando nuestro sistema. (`service auditd restart`)

Ahora vamos a configurar auditd para que no nos falle Docker-bench, para ello creamos el archivo `/etc/docker/*daemon.json`* y añadimos estas líneas: 

```bash
{
    "icc": false,
    "userns-remap": "default",
    "log-driver": "syslog", 
    "disable-legacy-registry": true,
    "live-restore": true,
    "userland-proxy": false,
    "no-new-privileges": true
   }
```

![3.JPG](https://github.com/mariadgt/PuestaEnProduccionSeguraA/UT3.PC01/img/3.jpg)

## Trivy.

Es una herramienta que analiza las vulnerabilidades del software en los contenedores, se utiliza para escanear imágenes y proporcionar vulnerabilidades conocidas y recomendaciones para solucionarlas.

Instalamos trivy con el siguiente comando:

```bash
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main"  >  /etc/apt/sources.list.d/trivy.list
sudo apt update
sudo apt install trivy
```

Vamos a hacer un testeo a un dockerfile que tengamos por aqui:

```bash
trivy config Dockerfile
```

![4.JPG](https://github.com/mariadgt/PuestaEnProduccionSeguraA/UT3.PC01/img/4.jpg)

> Nos avisa que creemos un usuario que no sea root para ejecutar las cosas del dockerfile.
> 

## Análisis de imágenes.

A continuación vamos a analizar imágenes de wordpress de diferentes versiones.

Descargamos dos imágenes, la última versión y la versión 4.6.

Vamos a compararlas:

`trivy image wordpress:latest`

![5.JPG](https://github.com/mariadgt/PuestaEnProduccionSeguraA/UT3.PC01/img/5.jpg)

`trivy image wordpress:4.6`

![6.JPG](https://github.com/mariadgt/PuestaEnProduccionSeguraA/UT3.PC01/img/6.jpg)

Podemos comprobar que aún en la última versión no se han encontrado tantos errores como en la versión 4.6, esta tiene un gran número de errores desconocidos en comparación con la última. Vemos también que en la versión más reciente aún no se han solucionado los problemas encontrados mientras que en la 4.6 vemos que ya tiene solución.
