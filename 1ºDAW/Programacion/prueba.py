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
            linea = linea + "%" * i + str(indice)
            i -= 1
        print(linea)
    indice -= 1


'''
   1 2 2 2 2 2 2 2 2 2 2 1
    1 2 3 3 3 3 3 3 3 3 2 1
    1 2 3 4 4 4 4 4 4 3 2 1
    1 2 3 4 palabra 4 3 2 1
    1 2 3 4 4 4 4 4 4 3 2 1
    1 2 3 3 3 3 3 3 3 3 2 1
    1 2 2 2 2 2 2 2 2 2 2 1

'''


numero = int(input("Introduce un numero entero: "))
palabra = input("Introduce una palabra: ")

ancho = 2 * numero - 2 + len(palabra)
fila = 1

while fila <= 2 * numero - 1:
    
    if fila <= numero:
        i = fila
    else:
        i = 2 * numero - fila
    linea = ""
    n = 1
    while n <= i:
        linea = linea + str(n) + " "
        n += 1
    if i == numero:
        linea = linea + palabra + " "
    else:
        n = 1
        while n <= ancho - 2 * i:
            linea = linea + str(i + 1) + " "
            n += 1
    n = i
    while n >= 1:
        linea = linea + str(n) + " "
        n -= 1

    print(linea)
    fila += 1