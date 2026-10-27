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
patron = ""
linea_num = ""
linea_ast= ""
num = numero
while indice <= numero*2-1:
    if indice <= numero:
        linea_num = str(indice) + " - "
        i = 2
        while i <= indice:
            linea_num = linea_num + str(indice) *i + " - "
            i += 1
        print(linea_num)
        if indice != numero:
            linea_ast = num * "* "
            num -=1
            print(linea_ast)
    else:
        if indice != numero:
            linea_ast = num * "* "
            num += 1
            print(linea_ast)
            
    indice += 1






"numero*2-1"