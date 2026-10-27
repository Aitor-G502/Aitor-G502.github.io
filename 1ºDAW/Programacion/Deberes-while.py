''' 1º
Imagina 4 pizzes que t’agradin, emmagatzema-les dins tipus llista i utilitza el bucle for per imprimir cadascun del nom d’aquestes pizzes.

'''

lista_pizza = ["Margarita", "Jamon", "Cuatro quesos", "Diavola"]

for a in lista_pizza:
    print(f'{a}')
print()
''' 1º a
Modifica el bucle per tal de que en comptes de només imprimir el nom de la pizza, imprimeixi una oració com per exemple ‘M’agrada la pizza de pepperoni’.
'''

for a in lista_pizza:
    print(f'Me encanta la pizza {a}')
print()
''' 1º b
Afegeix una línia que imprimeixi ‘M’encanten les pizzes’ una vegada que surtis del bucle.
'''
indice = 0

for a in lista_pizza:
    print(f'Me encanta la pizza {a}')
    indice +=1
    if indice == len(lista_pizza):
        print("Me encantan las pizzas")
    else:
        continue
print()
''' 2º
Escriure un programa que demani a l'usuari un nombre enter positiu i mostri per pantalla tots els números imparells des d'1 fins a aquest nombre separats per comes.
'''
num = int(input("Introduce un numero entero positivo: "))
num_imp = 1

while num >= num_imp:
    print(f'{num_imp}, ')
    num_imp += 2
print()
''' 3º 
Escriure un algorisme en Python que imprimeixi els 10 primers números parells començant a 2 i imprimiu també els seus respectius cubs
'''
lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for a in lista_pares:
    print(f"{a} - {a**3}")
print()

''' 3º a
Modifica aquest programa perquè en comptes d’imprimir els 10 primers nombres parells, imprimeixi els primers n nombres parells on n es un enter positiu introduït per teclat.

'''
num_par = int(input("Introduce un numero par: "))
par = 0

while num_par >= par:
    print(f'{par} - {par ** 3}')
    par += 2
print()
''' 4º
Realitza un programa que primer, llegeixi una frase per teclat i segón, que compti el nombre de paraules que té aquesta frase. 
Recorda que hauràs d’utilitzar mètodes built-in de la classe String i de la clase List a més d’utilitzar el bucle for.
'''
''' frase = input("Introduce una frase: ")

for a in frase:
    print(f'Tu frase {frase} tiene {frase.count} palabras') '''

''' 5º
Escriure un programa que demani a l'usuari un número sencer i mostri per pantalla un triangle rectangle com el de més avall, d'alçada el número introduït
'''
num_intr = int(input('Introduce un numero entero: '))
num_index = 0

while num_intr >= num_index:
    print(f'{num_index *'*'}')
    num_index += 1
print()
''' 6º
Escriure un programa que demani a l’usuari una paraula i la mostri per pantalla 10 vegades.

'''

palabra = input("Introduce una palabra: ")
indice_6 = 1

while indice_6 <= 10:
    print(palabra)
    indice_6 += 1
print()
''' 6º a
Modifica aquest programa perquè a l’usuari se li demani per teclat el nombre de vegades que vol repetir la paraula i la repeteixi tantes vegades com les introduïdes per l’usuari.
'''
palabra = input("Introduce una palabra: ")
multi = int(input("Introduce el numero de veces que quieres que se repita tu palabra: "))
indice_6 = 1

while indice_6 <= multi:
    print(palabra)
    indice_6 += 1
print()  
''' 7º
Fes un programa que llegeixi un nombre sencer per teclat i per pantalla imprimeixi tots els nombres primers des de l’1 fins al nombre introduït.
'''
numero = int(input("Introduce un numero entero: "))
indice = 1

while indice <= numero:
    print(indice)
    indice += 1
print()
''' 7º a
Modifica aquest programa per a que comprovi si el nombre introduït sigui un nombre sencer, en cas contrari s’imprimirà per pantalla el missatge
‘El nombre introduït no és un nombre sencer’.
'''
numero = int(input("Introduce un numero entero: "))
indice = 1

while indice <= numero:
    print(indice)
    if numero != int:
        print("El numero introducido no es un numero entero")
    indice += 1
print()
''' 8º 
Es col·loca un capital C, a un interès I (que oscil·la entre 0 i 100), durant M anys i es vol saber quan s'hi haurà convertit aquest capital en “M” anys, 
sabent que és acumulatiu (se refiere al interés, es decir, que cuando se calcule el interés en un año determinado, 
se calculará respecto a la cantidad original más las cantidades de los intereses de los años anteriores). 
Crea un programa utilitzant el bucle for que ens calculi l’interés acumulat d’aquest capital. El capital C i l'interès I s'hauran d’introduir per teclat.
'''

capital = float(input("Introduce tu capital: "))
intereses = float(input("Introduce el tipo de interes: "))
años = int(input("Introduce un numero de años: "))
indice = 0

while indice <= años:
    capital = capital * (intereses / 100)
    indice += 1
print(f'Tu capital despues de {años} años con un interes acumulativo de {intereses} es de {capital}')
print()

''' 9º
Crea un programa que calculi la suma de tots els divisors (sencers) d’un nombre sencer introduït per teclat 
(recorda que els divisors poden ser com a molt grans fins a la meitat del nombre introduït).
'''
numero_entero = int(input("Introduce un numero entero: "))
divisor = 1
indice = 0

while numero_entero >= indice:
    if numero_entero % divisor == 0:
        print(f'{divisor} es divisor de {numero_entero}')
    divisor += 1
    indice += 1
print()
''' 10º
Crea un programa que demani un text per teclat i que la sortida sigui el text invertit.
 No podrás fer servir la sintaxi [::-1] per invertir aquest texte sinó que hauràs de llegir-lo caràcter a caràcter i invertir-lo amb el bucle for.
'''
'''
texto = input("Introduce un texto: ")

for a in texto:
    print("a") '''


''' 11º
Imprimeix el següent patró utilitzant el bucle for, les dimensions del patró dependran d’un nombre introduït per teclat
'''
'PREGUNTAR'


''' 12º
Escriu un programa que donat un nombre sencer introduït per teclat imprimeixi tots els nombres primers des del número 1 fins a aquest nombre. 
numero = int(input('Introduce un numero entero: '))
contador = 0 

while numero >= contador:   
'''

''' 13º
Crea un programa utilitzant el bucle for que compti el nombre de xifres que té un número sencer introduït per teclat.
'''
numero_entero = input("Introduce un numero entero: ")

contador = 1

while contador < len(numero_entero):
    contador += 1

print(f'El numero tiene {contador} cifras')

''' 14º
Escriu un programa que pregunti quants números s'introduiran, demaneu aquests números, 
i mostri un missatge cada vegada que un nombre no sigui més gran que el primer nombre introduït.
cuantosnum = int(input("Cuantos numeros se introduciras: "))

demnum = int(input(f'Introduce {cuantosnum} numeros: '))

contador = 0

while cuantosnum >= contador:
    if demnum[0] > demnum[1]:
        print("El numero introducido es mas pequeño que el numero anterior")
        demnum
    else:
        continue

'''

''' 15º
Escriviu un programa que pregunti quants números s'introduiran, demaneu aquests números, 
i mostri un missatge cada vegada que un nombre no sigui més gran que l'anterior.
cuantosnum = int(input("Cuantos numeros se introduciras: "))

demnum = int(input(f'Introduce {cuantosnum} numeros: '))

contador = 0

while cuantosnum >= contador:
    if demnum[0] > demnum[1]:
        print("El numero introducido es mas pequeño que el numero anterior")
        demnum
    else:
        continue
'''

''' 16º

'''



''' 20º

'''
frase = input("Introduce una frase: ")

vocales = "AEIOUaeiou"

vocal = 0
index = 0

while index < len(frase):
    if frase[index] == vocal[0] or frase[index] == vocal[1] or frase[index] == vocal[2] or frase[index] == vocal[3] or frase[index] == vocal[4] or frase[index] == vocal[5] or frase[index] == vocal[6] or frase[index] == vocal[7] or frase[index] == vocal[8] or frase[index] == vocal[9]:
        vocal += 1
    index +=1

print(f'En la frase {frase}, el numero de vocales que aparecen es de {vocal}')

''' 1º while
Escriviu un programa que pregunteu una vegada i una altra si voleu continuar amb el programa, sempre que es contesti exactament sí (en minúscules i amb titlla).
'''
pregunta = input("¿Quieres continuar con el programa?: ")


while pregunta == "sí":
    pregunta2 = input("¿Estas seguro de que deseas continuar?: ")
    if pregunta2 == 'sí':
        print("Gracias por contestar a nuestra pregunta.")
        break
    else:
        continue
print()

''' 2º while
Escriviu un programa que pregunteu una vegada i una altra si voleu continuar amb el programa, 
sempre que es contesti un sí, podrà ser un ‘si’ en minúscula o majúscula parcialment o totalment o amb accent o sense
'''
pregunta = input("¿Quieres continuar con el programa?: ")


while pregunta == "sí" or pregunta == 'si' or pregunta == 'Si' or pregunta == "SI":
    pregunta2 = input("¿Estas seguro de que deseas continuar?: ")
    if pregunta2 == 'sí' or pregunta2 == 'si' or pregunta2 == 'Si' or pregunta2 == "SI":
        print("Gracias por contestar a nuestra pregunta.")
        break
    else:
        continue
print()


''' 3º while
Realitza un programa que llegeixi dos números per teclat i permeti triar entre 3 opcions en un menú:
Mostra una suma dels dos números
Mostrar una resta dels dos números (el primer menys el segon)
Mostrar una multiplicació dels dos números
En cas de no introduir una opció vàlida, el programa informarà que no és correcta.


'''
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

menu = ''' Introduce una de las siguientes opciones:
    1 - Se sumaran los numeros introducidos anteriormente
    2 - Se restaran los numeros introducidos anteriormente
    3 - Se multiplicaran los numeros introducidos anteriormente
    4 - Salir
'''

opciones = input(menu)

while True:
    match opciones:
        case '1':
            resultado = num1 + num2
            print(f'La suma de {num1} y {num2} es de {resultado}')
        case '2':
            resultado = num1 - num2
            print(f'La resta de {num1} y {num2} es de {resultado}')
        case '3':
            resultado = num1 * num2
            print(f'El resultado de multiplicar {num1} y {num2} es de {resultado}')
        case '4':
            print(f'Gracias por usar nuestro programa')
            break
        case _: 
            print("No has introducido un valor valido")
    print()
    opciones = input(menu)

''' 4º
Realitza un programa que llegeixi un nombre imparell per teclat. Si l'usuari no introdueix un nombre imparell, 
s'ha de repetir el procés fins que l'introdueixi correctament.
'''
   
numimpar = int(input("Introduce un numero impar: "))



while numimpar % 2 == 0:
    numimpar = int(input("Ese numero no es impar, porfavor introduce otro numero impar: "))

print(f"Tu numero {numimpar} es un numero impar")

''' 5º
Realitza un programa que sumi tots els números sencers parells des del 0 fins al 100.
'''
numero1 = 0
numero2 = 100

numeroactual = numero1
suma = 0

while numeroactual <= numero2:
    suma += numeroactual
    numeroactual += 2

print(f'La suma de los numeros enteros entre {numero1} y {numero2} es de {suma}')

''' 6º while
Realitza un programa que demani a l'usuari un nombre enter del 0 al 9 i que mentre el número no sigui correcte es repeteixi el procés. 
Després heu de comprovar si el número es troba a la llista de números i notificar-ho
'''

nument = int(input("Introduce un numero entero entre el 0 y el 9: "))

listanument = [1, 3, 6, 9]

while True:
    match nument:
       case 0:
            print("No has conseguido acertar un numero dentro de la lista")
       case 2:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 4:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 5:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 7:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 8:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case _:
            print("Enhorabuena, has conseguido acertar un numero en la lista")
            break
    print()
    nument = int(input("Introduce un numero entero entre el 0 y el 9: "))

''' 7º
Donades dues llistes, has de generar una tercera amb tots els elements que s'hi repeteixin en cada una d’elles 
(és a dir, els elements repetits de llista 1 + els elements repetits de llista 2), però no s'ha de repetir cap element a la nova llista.
'''
lista1 = [1,1,2,3,4,5,5,6,7,7,8,9,9,1,11,12,13,14,15,16,15,1,2]
lista2 = [1,2,2,3,3,4,5,6,7,7,8,8,9,9]
