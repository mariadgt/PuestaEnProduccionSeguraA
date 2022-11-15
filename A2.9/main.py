"""
Definir un histograma procedimiento() que tome una lista de números enteros e
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
lo siguiente:
"""
numeros= [7, 2, 0, 7, 2]
def procedimiento(numeros):
    cadena= ""
    for x in numeros:
        print(x * "x")
procedimiento(numeros)

