"""
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres.
"""
lista= ["tomate", "patata", "lechuga", "queso"]
numero= 5
def filtrar_palabras(lista, numero):
    caracteres= numero
    palabras= []
    for x in lista:
        if len(x) > caracteres:
            palabras.append(x) #append añade elementos a una lista
    print(palabras)
filtrar_palabras(lista, numero)