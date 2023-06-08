"""
Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
numeros= [1, 2, 3, 4]
def sum(numeros):
    suma= 0
    for x in numeros:
        suma += x
    print(suma)
sum(numeros)
def mul(numeros):
    multi= 1
    for x in numeros:
        multi *= x
    print(multi)
mul(numeros)
