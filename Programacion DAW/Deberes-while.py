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