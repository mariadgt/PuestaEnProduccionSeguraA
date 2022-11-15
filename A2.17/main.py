"""
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra
"""
palabra = input()

def contar_vocales(palabra):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for x in palabra:
        if x == "a":
            a = a + 1
        elif x == "e":
            e = e + 1
        elif x == "i":
            i = i + 1
        elif x == "o":
            o = o + 1
        elif x == "u":
            u = u + 1
    print("a =", a)
    print("e =", e)
    print("i =", i)
    print("o =", o)
    print("u =", u)
contar_vocales(palabra)
