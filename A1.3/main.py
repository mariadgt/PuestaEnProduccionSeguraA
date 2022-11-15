"""
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
"""
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for numero in numeros:
    if numero % 3 == 0:
        print(numero)
