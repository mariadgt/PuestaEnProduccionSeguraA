"""
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)
"""
lista = ["maria", "antonio", "david", "Alvaro"]
letra = input()
contador = 0
for i in lista:
    if (letra == (i[0]).upper()) or (letra == (i[0]).lower()):
        contador += 1
print(contador)
