"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio.
"""
frase= input()

def contarcadena(frase):
    numero = 0
    for x in frase:
        numero = numero +1
    print(numero)
contarcadena(frase)