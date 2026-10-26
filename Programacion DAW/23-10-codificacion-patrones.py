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


while numero >= indice:
    if indice > 1:
        linea = str(indice) + " - "
        i = 2
        while i <= indice:
            linea = linea + str(indice) * i + " - "
            i += 1
        print(linea)
    else:
        print(f'{indice} - ')
    indice += 1
    if num > 2:
        print(f'{(num *'* ')} ')
    else:
        print(f'{(num *'* ')} ')
        num -= 1
    num -= 1


''' 4º
5 * * * * 5 * * * 5 * * 5 * 5
4 %%% 4 %% 4 % 4
3 * * 3 * 3
2 % 2
1
2 * 2
3 %% 3 % 3
4 * * * 4 * * 4 * 4
5 %%%% 5 %%% 5 %% 5 % 5

'''

numero_2 = int(input("Introduce un numero entero: "))
indice = numero_2

while indice >= 1:
    
    if indice %2 != 0:
        linea = str(indice)
        i = indice - 1
        while i >= 1:
            linea = linea + " * " * i + str(indice)
            i -= 1
        print(linea)
    else:
        linea = str(indice)
        i = indice - 1
        while i >= 1:
            linea = linea + " % " * i + str(indice)
            i -= 1
        print(linea)
    indice -= 1