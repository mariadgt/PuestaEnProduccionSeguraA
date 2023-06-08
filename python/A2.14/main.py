"""
Construir un pequeño programa que convierta números binarios en enteros.
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""
print("Conversor de binario a decimal:")
binario = input()
vuelta = binario[::-1]


def binario_a_decimal(vuelta):
    posicion = 0
    multi = 0
    for x in vuelta:
        elevar = 2 ** posicion
        posicion = posicion + 1
        if x == '1':
            multi += elevar
    print(multi)


binario_a_decimal(vuelta)

print("¿En que año estamos?:")
ano_actual = int(input())
print("¿Como se llama la 1º persona?:")
persona1 = input()
print("¿En que año nació?:")
ano_persona1 = int(input())
print("¿Como se llama la 2º persona?:")
persona2 = input()
print("¿En que año nació?:")
ano_persona2 = int(input())
print("¿Como se llama la 3º persona?:")
persona3 = input()
print("¿En que año nació?:")
ano_persona3 = int(input())

def anos_tiene(ano_actual, ano_persona1, ano_persona2, ano_persona3):
    resta1 = ano_actual - ano_persona1
    resta2 = ano_actual - ano_persona2
    resta3 = ano_actual - ano_persona3
    print(persona1, ":", resta1)
    print(persona2, ":", resta2)
    print(persona3, ":", resta3)
anos_tiene(ano_actual, ano_persona1, ano_persona2, ano_persona3)
