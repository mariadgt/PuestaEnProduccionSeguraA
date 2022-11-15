"""
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
frase= "estoy probando"
def reverse(frase):
    vuelta = ""
    for x in frase:
        vuelta = x + vuelta
    print(vuelta)

reverse(frase)
