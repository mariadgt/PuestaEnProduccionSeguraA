"""
Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
"xxxxx".
"""
numero= int(input())
def generar_n_caracteres(numero):
    cadena = ""
    for x in range(numero):
        cadena += "x"
    print(cadena)
generar_n_caracteres(numero)