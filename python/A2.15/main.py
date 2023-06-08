"""
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""
edades = (3, 13, 53, 24, 15, 36, 76, 12, 20, 36)
mostrar = 0
for x in edades:
    if x > 20:
        mostrar = mostrar +1
print(mostrar)
