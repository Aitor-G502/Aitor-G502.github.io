# 1 Escriviu un programa que pregunteu una vegada i una altra si voleu continuar amb el programa, 
# sempre que es contesti exactament sí (en minúscules i amb titlla).

pregunta = input("¿Quieres continuar con el programa?: ")



while pregunta == "sí":
    pregunta2 = input("¿Estas seguro de que deseas continuar?: ")
    break

print("Gracias por contestar a nuestra pregunta.")


# 2 Escriviu un programa que pregunteu una vegada i una altra si voleu continuar amb el programa, sempre que es contesti un sí, 
# podrà ser un ‘si’ en minúscula o majúscula parcialment o totalment o amb accent o sense

preguntaej2 = input("¿Quieres continuar con el programa?: ")



while (pregunta == "sí") or (pregunta == "si") or (pregunta == "Sí") or (pregunta == "Si") or (pregunta == "SÍ") or (pregunta == "SI"):
    pregunta2 = input("¿Estas seguro de que deseas continuar?: ")
    break

print("Gracias por contestar a nuestra pregunta.")

# 3 Realitza un programa que llegeixi dos números per teclat i permeti triar entre 3 opcions en un menú:
# Mostra una suma dels dos números
# Mostrar una resta dels dos números (el primer menys el segon)
# Mostrar una multiplicació dels dos números
# En cas de no introduir una opció vàlida, el programa informarà que no és correcta.

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
    

# 4 Realitza un programa que llegeixi un nombre imparell per teclat. Si l'usuari no introdueix un nombre imparell, 
# s'ha de repetir el procés fins que l'introdueixi correctament.

numimpar = int(input("Introduce un numero impar: "))



while numimpar % 2 == 0:
    numimpar = int(input("Ese numero no es impar, porfavor introduce otro numero impar: "))

print(f"Tu numero {numimpar} es un numero impar")



print()
# 5 Realitza un programa que sumi tots els números sencers parells des del 0 fins al 100.
print("El siguiente programa realizara la suma de todos los numeros enteros entre el 0 y el 100")

numero1 = 0
numero2 = 100

numeroactual = numero1
suma = 0

while numeroactual <= numero2:
    suma += numeroactual
    numeroactual += 1

print(f'La suma de los numeros enteros entre {numero1} y {numero2} es de {suma}')

# 6 Realitza un programa que demani a l'usuari un nombre enter del 0 al 9 i que mentre el número no sigui correcte es repeteixi el procés. 
# Després heu de comprovar si el número es troba a la llista de números i notificar-ho. La llista de nombres que faràs servir és [1, 3, 6, 9].

nument = int(input("Introduce un numero entero entre el 0 y el 9: "))

listanument = [1, 3, 6, 9]

while True:
    match nument:
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


# 7 Donades dues llistes, has de generar una tercera amb tots els elements que s'hi repeteixin en cada una d’elles 
# (és a dir, els elements repetits de llista 1 + els elements repetits de llista 2), però no s'ha de repetir cap element a la nova llista. 
# Les dues llistes que utilitzaràs són (no utilitzeu el tipus set()):

lista1 = [1,1,2,3,4,5,5,6,7,7,8,9,9,1,11,12,13,14,15,16,15,1,2]
lista2 = [1,2,2,3,3,4,5,6,7,7,8,8,9,9]

lista3 = []

contador = 1

while contador < 