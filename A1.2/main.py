"""
Solicitar al usuario dos valores:
● numero1 (int)
● numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
siguiente):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
¿Cuál es el código del requerimiento solicitado?
"""
numero1= int(input("Proporciona el numero 1:"))
numero2= int(input("Proporciona el numero 2:"))
if numero1 < numero2:
    print("El numero mayor es:",numero2)
else:
    print("El numero mayor es:",numero1)