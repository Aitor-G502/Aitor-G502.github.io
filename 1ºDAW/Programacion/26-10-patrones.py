'''
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
            linea = linea + " " + "%"  * i + " " +  str(indice)
            i -= 1
        print(linea)
    indice -= 1
    
indice = 2

while indice <= numero_2:
    if indice % 2 != 0:
        linea = str(indice)
        i = indice - 1
        while i >= 1:
            linea = linea + " " + "%" * i + " " + str(indice)
            i -= 1
        print(linea)
        
    else:
        linea = str(indice)
        i = indice - 1
        while i >= 1:
            linea = linea + " * " * i + str(indice)
            i -= 1
        print(linea)
    indice += 1

'''
    1        
   2*2       
  3-3-3
 4*4*4*4
5-5-5-5-5
 4*4*4*4
  3-3-3
   2*2
    1

'''
numero = int(input("Introduce un numero entero: "))
indice = 1

while numero  >= indice:
    print(indice)
    indice += 1
