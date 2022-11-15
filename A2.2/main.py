"""
Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos.
"""
numero1= int(input())
numero2= int(input())
numero3= int(input())
def max(numero1, numero2, numero3):
    if numero1 < numero2 and numero3 < numero2:
        print("El numero mayor es:", numero2)
    elif numero1 < numero3 and numero2 < numero3:
        print("El numero mayor es:", numero3)
    else:
        print("El numero mayor es:", numero1)
max(numero1, numero2, numero3)