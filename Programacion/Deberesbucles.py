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
    numLin = numLin + 2

# 3 Escriure un algorisme en Python que imprimeixi els 10 primers números parells començant a 2 i imprimiu també els seus respectius cubs. Per exemple: 2 – 8; 4 – 64; 6 – 216 …
#Modifica aquest programa perquè en comptes d’imprimir els 10 primers nombres parells, imprimeixi els primers n nombres parells on n es un enter positiu introduït per teclat.


numpar = int(input("Introduce un numero par: "))

num = 2

contador = 1

while contador <= numpar:
    print(f'{num} - {num**3}')
    num = num + 2
    contador = contador + 1

# 4 Realitza un programa que primer, llegeixi una frase per teclat i segón, que compti el nombre de paraules que té aquesta frase. 
# Recorda que hauràs d’utilitzar mètodes built-in de la classe String i de la clase List a més d’utilitzar el bucle for.
num4 = input("Escribe una frase aqui: ")

listanum4 = list(num4)

i = 1

palabrasnum4 = 1

for element in listanum4:
    if element == " ":
        palabrasnum4 = palabrasnum4 + 1
    i = i + 1
print(f'Tu frase contiene {palabrasnum4} palabras')

num4 = input("Escribe tu frase aqui: ")

listanum4 = list(num4)

palabranum4 = 1

i = 1

for element in listanum4:
    if element == " ":
        palabranum4 = palabranum4 + 1
    i = i +1
print(f'Tu frase tiene {palabranum4} palabras')


# 5 Escriure un programa que demani a l'usuari un número sencer i mostri per pantalla un triangle rectangle com el de més avall, d'alçada el número introduït. 
# La imatge següent mostra l’exemple de la sortida del programa si introduïm el número 5.
#* 
#** 
#*** 
#**** 
#*****

nument = int(input("Introduce un numero entero: "))
numentLin = 1

while numentLin <= nument:
    print(f'{numentLin*'*'}')
    numentLin = numentLin + 1



# 6 Escriure un programa que demani a l’usuari una paraula i la mostri per pantalla 10 vegades.
#Modifica aquest programa perquè a l’usuari se li demani per teclat el nombre de vegades que vol repetir la paraula i la repeteixi tantes vegades com les introduïdes per l’usuari.

palabra = input("Introduce una palabra: ")
veces = int(input("Introduce las veces que quieres que se repita: ")) 
mult = 1

while mult <= veces:
    print(f'{palabra}')
    mult = mult + 1

# Es demanar a l'usuari que introdueixi una cadena de caràcters per teclat y el bucle for haurà de processar aquesta cadena
# i crear-ne una de nova amb les lletres minúscules y majúscules alternades.
deberes = input("Escribe tu cadena de caracteres aqui: ")

#Es demanar a l'usuari que introdueixi una cadena de caràcters per teclat y el bucle for haurà de processar aquesta cadena
# i crear-ne una de nova amb les lletres minúscules y majúscules alternades.

deberes = input("Escribe tu cadena de caracteres: ")

listadeberes = list(deberes)

nuevadeberes = []

ñ = 1

palabradeberes = ""

listadeberes = list(deberes)

nuevadeberes = []

palabradeberes = ""

ñ = 1

for letradeberes in listadeberes:
    if ñ %2 == 0:
        nuevadeberes.append(letradeberes.lower())
    else:
        nuevadeberes.append(letradeberes.upper())
    ñ = ñ+1

for letradeberes2 in nuevadeberes:
    palabradeberes = palabradeberes + letradeberes2

for letradeberes2 in nuevadeberes:
    palabradeberes = palabradeberes + letradeberes2
print(f'{palabradeberes}')



cadena = input("Escribe tu cadena de caracteres: ")

cadenaalt = ""

ismayus = True

for char in cadena:
    if ismayus:
        cadenaalt += char.upper()
    else:
        cadenaalt += char.lower()
    ismayus = not ismayus

print(f'La cadena resultante de {cadena} es:{cadenaalt}')

print()

cadena2 = input("Escripe tu cadena de caracteres: ")

cadenaalt2 = ""

ismayus2 = True

indice = 0

while indice <= len(cadena2) -1:
    if ismayus2:
        cadenaalt2 += cadena[indice].upper()
    else:
        cadenaalt2 += cadena[indice].lower()
    ismayus2 = not ismayus2
    indice += 1

    print(f'La cadena resultante de {cadena2} es:{cadenaalt2}.')