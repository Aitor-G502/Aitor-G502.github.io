# 1. Imagina 4 pizzes que t’agradin, emmagatzema-les dins tipus llista i utilitza el bucle for per imprimir cadascun del nom d’aquestes pizzes.
# Modifica el bucle per tal de que en comptes de només imprimir el nom de la pizza, imprimeixi una oració com per exemple ‘M’agrada la pizza de pepperoni’.
# Afegeix una línia que imprimeixi ‘M’encanten les pizzes’ una vegada que surtis del bucle.

pizza =  ''' Introduce un el numero de tu pizza favorita
1 - Margarita 
2 - Proccuito 
3 - Diavola 
4 - 4 Quesos
5 - Salir
'''
opcio = input(pizza)


while True:
    match opcio:
        case "1":
            print("Te encantan las pizzas Margaritas")
        case "2":
            print("Te encantan las pizzas Proccuito")
        case "3":
            print("Te encantan las pizzas Diavolas")
        case "4":
            print("Te encantan las pizzas 4 Quesos")
        case "5":
            print("Graicas por tu apoyo incondicional a las pizzas")
            break
        case _:
            print("No es un numero valido")

    print()
    opcio = input(pizza)

    
# 2 Escriure un programa que demani a l'usuari un nombre enter positiu i mostri per pantalla tots els números imparells des d'1 fins a aquest nombre separats per comes.


n = int(input("Introduce un numero entero: "))
numLin = 1

while numLin <= n:
    print(f'{numLin},')
    numLin = numLin + 1

# 3 Escriure un algorisme en Python que imprimeixi els 10 primers números parells començant a 2 i imprimiu també els seus respectius cubs. Per exemple: 2 – 8; 4 – 64; 6 – 216 …
#Modifica aquest programa perquè en comptes d’imprimir els 10 primers nombres parells, imprimeixi els primers n nombres parells on n es un enter positiu introduït per teclat.