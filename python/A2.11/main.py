"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga
"""
lista= ["tomate", "patata", "lechuga", "queso"]
def mas_larga(lista):
    max= 0
    palabra= None
    for x in lista:
        if len(x) > max:
            max = len(x)
            palabra= x
    print(palabra)
mas_larga(lista)
