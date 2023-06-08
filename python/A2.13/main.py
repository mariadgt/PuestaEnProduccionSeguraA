"""
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene
"""
cadena= input()
def letras_mayusculas(cadena):
    tiene= 0
    for x in cadena:
        if x == x.upper(): #upper para saber si una letra es mayúsculas
            tiene= tiene +1
    print(tiene)
letras_mayusculas(cadena)