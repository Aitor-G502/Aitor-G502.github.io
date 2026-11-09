'''
Holas ***** holAS **** HOLas *** hOLAS ** HOLAS *
holaS #### HOlas ### hoLAS ## HOLAs #
Holas *** holAS ** HOLas *
holaS ## HOlas #
Holas *
'''

palabra = input("Introduce una palabra: ")
numero = int(input("Introduce un numero entero (hasta 9): "))
while numero > 9:
    numero = int(input("Tiene que ser un numero entero no mayor a nueve, vuelve a introducir un numero: "))
salto = " "
index = numero
print()

while index >=  1:
    if index %2 != 0:
        linea = palabra
        i = index
        while i > 1:
            linea = linea + salto + "*" * i + salto + palabra
            i -= 1
        print(linea + " *")
        
    else:
        linea = palabra
        i = index
        while i > 1:
            linea = linea + salto + "#" * i + salto + palabra
            i -= 1
        print(linea + " #")
    index -= 1
    


print()