"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False.
"""
letra= input()
def vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("True")
    else:
        print("False")
vocal(letra)