"""
Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""
numero1= int(input())
numero2= int(input())
def max(numero1, numero2):
    if numero1 < numero2:
        print("El numero mayor es:", numero2)
    else:
        print("El numero mayor es:", numero1)
max(numero1, numero2)


