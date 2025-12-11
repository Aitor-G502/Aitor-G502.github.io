#Exercicis de teoria:
'''1 - Explica els diferents tipus de contenidors de dades i les seves característiques i, per tant, les seves diferències. 1 punt
print(), nos permite imprimir por pantalla
input(), nos permite detectar lo que se escribe por teclado
list.appen(), añade un solo elemento al final de una lita [1, 2, [3, 4]]
list.remove(), elimina la primera aparicion de un elemento en una lista [1, 1, 2, 3] -> [1, 2, 3] en caso de elegir el 1
list.reverse(), invierte una lista [1, 2, 3] -> [3, 2, 1]
list.insert(), añade un elemnto en una posicion determinada sin afectar al resto de la lista, queremos añadir el 3 a una lista -> [1, 2, 4] -> [1, 2, 3, 4], a diferencia del appen,
este nos permite añadir elementos sin que cuenten como 1 solo elemento
list.clear(), nos permite eliminar todos los elementos de una lista 
list.count(), nos permite contar el numero de elementos de una lista desde su indice (0).
'''

'''2 - Digues quin tipus de dades natius de Python hem vist a classe i explica’ls. 0.75 punts.
string,en python se ve como str, es un tipo de dato que se utiliza para caracteres hexadecimales com "A" o "2" para que un numero cuente como str, debe de estar entre comillas
integrer, en python se ve como int, es un tipo de dato que se utiliza para caracteres numericos enteros como 1, 2 o 3, no se puede utilizar para letras
float, en python se ve como float, es un tipo de dato que se utiliza para caractetes numericos decimales como 0'1, 0'2
boleanos, en python se ve como bol, es un tipo de dato de verdadero o falso que el verdadero se representa como 0 y falso como 1
binarios, en python se ve como bin, tipo de dato numerico que solo cuenta con un 0 y un 1
'''

#Exercicis de condicionals:
'''3 - Crea un petit programa que demani que l’usuari introdueixi per teclat una  opció de l’1 al 5 (pot ser processat com a enter o com a caràcter) i que imprimeixi per pantalla 
 “Has introduït l'opció -nombre introduït-” o, en el cas de no introduir una opció correcte imprimeixi “No has introduït una opció vàlida”. 1’75 punts'''

ej3 = (input("Introduce un numero del 1 al 5: "))

if ej3 == "1":
    print(f'Has introducido la opcion {ej3}')
elif ej3 == "2":
    print(f'Has introducido la opcion {ej3}')
elif ej3 == "3":
    print(f'Has introducido la opcion {ej3}')
elif ej3 == "4":
    print(f'Has introducido la opcion {ej3}')
elif ej3 == "5":
    print(f'Has introducido la opcion {ej3}')
else:
    print(f'No has introducido una opcion valida')

'''4 - (Exercici amb condicionals). Escriu un programa que llegeixi una lletra per teclat i digui si es tracta d’una vocal. Haureu de tenir en compte les majúscules també, 
 no serà necessari tenir en compte les vocals amb accent o altres. Una altra cosa que haurà de fer el programa serà la d’imprimir un missatge d’error 
 “Has introduït més d’una lletra” si l’usuari introdueix 2 o més lletres com a missatge d’entrada. 1’75 punt'''

ej4 = input("Introduce 1 sola letra: ")
if ej4:
    match ej4:
        case "a":
            print("Has introducido una vocal")
        case "e":
            print("Has introducido una vocal")
        case "i":
            print("has introducido una vocal")
        case "o":
            print("Has introducido una vocal")
        case "u":
            print("Has introducido una vocal")
        case _:
            print("Has introducido mas de una letra o es una consonante")

    

'''5 - (Exercici amb condicionals). Crea una calculadora per donar-te un impost d’IRPF total a pagar en funció d’un salari introduït per l’usuari. 
 Una vegada que l’usuari introdueixi el seu salari (haurà de ser transformat en ‘float’) la calculadora fará el següent:
Si el salari és inferior o igual a 15000€ anuals, el’usuari no haurà de pagara res.
Si el salari és troba entre els 15000€ i els 30000€ (aquest darrer inclòs) l’usuari haurà de pagar el 17% d’aquest en IRPF (multiplica el salari per 0.17 i ja tens la quantitat).
Si el salari es troba entre els 30000€ i els 45000€ (aquest darrer inclòs) l’usuari haurà de pagar el 23% d’aquest en IRPF (multiplica el salari per 0.23 i ja tens la quantitat).
Si el salari és superior a 45000€ l’usuari haurà de pagar el 37% d’aquest salari en IRPF multiplica el salari per 0.37 i ja tens la quantitat). 2 punts'''

ej5 = float(input("Introduce tu salario anual: "))

if ej5 <= 15000:
    print("No tienes que pagar nada")
elif (ej5 > 15000) and (ej5 <= 30000):
    print(f'Tienes que pagar {ej5 * 0.17}€ de IRPF' )
elif (ej5 > 30000) and (ej5 <= 45000):
    print(f'Tienes que pagar {ej5 * 0.23}€ de IRPF')
elif (ej5 > 45000):
    print(f'Tienes que pagar {ej5 * 0.37}€ de IRPF')
#Exercicis de bucles:
'''6 - Crea un menú ‘infinit’ del qual només es pugui sortir quan l’usuari introdueix per teclat el número 3. Aquest menú haurà de tenir 3 opcions: 1.5 punts.
1a opció: ‘Introdueix el número 1 per saludar-te’, i si l’usuari introueix aquest número el programa haurà de contestar: ‘Hola que tal Pascual’.
2a opció: ‘Introdueix el número 2 per fer una suma’, llavors, demanará dos números per teclat i imprimirà per pantalla: “La suma del ‘num1’+ ‘num2’ és: ‘resultat de la suma’”.
3a opció: ‘Introdueix el número 3 per sortir d’aquest menú’, si el usuari introdueix el número 3, haurà d’imprimir ‘Adeu Mateu.’ i haurà de finalitzar.'''

ej6 = input('''Introduce un numero:
1. - Recibias un saludo
2. - Recibiras una suma
3. - Salir

''')


while True:
    match ej6:
        case '1':
            print("Hola que tal Pascual")
        case '2':
            suma = int(input("Escribe el primer numero: "))
            suma2 = int(input("Escribe el segundo numero: "))
            print(f'La suma de {suma} y {suma2} es de {suma + suma2}')
        case '3':
            print("Adeu Mateu")
            break
print(ej6)

'''7 - Realitza un programa que demani a l’usuari un nombre i un caràcter d’entrada i a partir d’aquests realitzi el següent patró (exemple per a nombre = 4 y per a caràcter = #) :
“””
1#
2##2##
3###3###3###
4 ####4####4####4####

1.25 punts.'''
