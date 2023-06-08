"""
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto. Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""
anio = int(input())
def es_bisiesto(anio):
    division = anio % 4
    division2 = anio % 100
    division3 = anio % 400
    if division == 0 and division2 != 0 or (division2 != 0 and division3 == 0):
        print("es bisiesto")
    else:
        print("no es bisiesto")

es_bisiesto(anio)