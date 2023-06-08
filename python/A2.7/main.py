"""
Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado.
"""
lista1= [7, 2, 0, 7, 2]
lista2= [1, 5, 3, 4, 5]
def superposicion(lista1, lista2):
    si= False
    for x in lista1:
        for y in lista2:
            if x == y:
                si= True
            else:
                si= False
    print(si)
superposicion(lista1, lista2)