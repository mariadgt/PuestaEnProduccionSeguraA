"""
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
más de 3 números o no sabemos cuántos números son. Escribir una función
max_in_list() que tome una lista de números y devuelva el más grande.
"""
numeros = [0,7,3,1,5,6,3,2,4]
def max_in_list(numeros):
    max = 0
    for x in numeros:
        if x > max :
            max = x
    print(max)
max_in_list(numeros)