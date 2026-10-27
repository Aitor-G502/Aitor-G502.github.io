''' 3º
1 - 
* * * *
2 - 22 -
* * *
3 - 33 - 333 -
* *
4 - 44 - 444 - 4444 -
* *
3 - 33 - 333 -
* * *
2 - 22 -
* * * *
1 - 

'''

numero = int(input("Introduce un numero entero: "))
indice = 1
num = numero
linea = []
while numero >= indice:
    if indice >= 1:
        linea = str(indice) + " - "
        i = 2
        while i <= indice:
            linea = linea + str(indice) * i + " - "
            i += 1
        print(linea, end="")
    else:
        print(f'{indice} - ')
    indice += 1
    if num > 2:
        print("\n"f'{(num *'* ')} ')
    elif num == numero - 1:
        print(end="")
    else:
        print("\n"f'{(num *'* ')}' ) 
        num -= 1
    num -= 1
    

indice = numero - 1
num = numero - indice + 1

while indice >= 1:
    if num > 2:
        print(f'{(num *'* ')} ')
    else:
        print(f'{(num *'* ')} ')
        num += 1
    num += 1
    if indice > 1:
        linea = str(indice) + " - "
        i = 2
        while i <= indice:
            linea = linea + str(indice) * i + " - "
            i += 1
        print(linea)
    else:
        print(f'{indice} - ')
    indice -= 1
    



