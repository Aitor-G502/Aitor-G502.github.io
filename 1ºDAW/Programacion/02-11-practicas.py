# 8 - Octavo ejercicio:
# El programa pide una palabra de como máximo 9 caracteres y 2 caracteres de relleno (se pide cada uno por separado).
# En el caso de que la palabra introducida fuera “palabra”, el primer caracter de relleno 
# fuera “*” y el segundo carácter de relleno fuera “-”, el patrón generado (por pasos sería)
'''
*-------*      -*******- 
*palabra*  --> -palabra-
*-------*      -*******- 

*---------*      -*********-
*         *      -         -
* palabra *      - palabra -
*         *      -         -
*---------*      -*********-

*-----------*      -***********-
*           *      -           -
*           *      -           -
*  palabra  *      -  palabra  -
*           *      -           -
*           *  --> -           -
*-----------*      -***********-

print("\033[2J\033[H", end="") == os.system('cls')(win) / os.system('clear)(linux)
'''
import os
import time

palabra = input("Introduce una palabra de un maximo de 9 letras: ")
while len(palabra) > 9:
    palabra = input("Sabes leer?, Introduce una palabra de un maximo de 9 letras: ")

simbolo1 = input("introduce el primer simbolo (solo 1): ")
while len(simbolo1) > 1:
    simbolo1 = input("Otra vez? Introduce solo 1 simbolo: ")

simbolo2 = input("Introduce el segundo simbolo (solo 1): ")
while len(simbolo2) > 1:
    simbolo2 = input("Otra vez? Introduce solo 1 simbolo: ")

index = 1
os.system('clear')

while index <= 3:
    print(simbolo1 , end="")
    print(simbolo2 * len(palabra) + simbolo1)
    while index == 1:
        print(simbolo1 + palabra + simbolo1)
        index += 1
    index += 1
time.sleep(1)
os.system('clear')

while index <= 6:
    print(simbolo2 , end="")
    print(simbolo1 * len(palabra) + simbolo2)
    while index == 4:
        print(simbolo2 + palabra + simbolo2)
        index += 1
    index += 1
time.sleep(1)
