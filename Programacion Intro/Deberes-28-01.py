# 15 Escriviu un programa que pregunti quants números s'introduiran, 
# demaneu aquests números, i digueu al final quants han estat parells i quants senars 
# a més d’imprimir una llista dels parells i una llista dels senars

numerope = int(input("Cuantos numeros desea introducir: "))


i = 0


pares = []

inpares = []

while i < numerope:
    numeroint = int(input("Introduce un numero: "))

    if numeroint %2 == 0:
        pares.append(numeroint)
    else:
        inpares.append(numeroint)
    i += 1

print(f'En total, han salido {len(pares)} numeros pares y {len(inpares)} numeros inpares')
print()
print(f'Lista pares: {pares}')
print()
print(f'Lista impares: {inpares}')


print()
# 16 Escriviu un programa que demani dos nombres enters i escriviu la suma de tots els enters des del primer número fins al segon. 

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

suma = 0
numactual = numero1

while numactual <= numero2:
    suma += numactual
    numactual += 1

print(f'La suma de los numeros entre {numero1} y {numero2} incluyendolos, es de {suma}.')


print()

#17 Milloreu el programa anterior fent que el programa escrigui la suma realitzada

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

suma = 0
numactual = numero1
resultado = ""

while numactual <= numero2:
    suma += numactual
    resultado += str(numactual)
    

    if numactual < numero2:
        resultado += " + "
    
    numactual += 1

print(f'La suma de los numeros entre {numero1} y {numero2} incluyendolos, es de {suma}.')
print()
print(f'La operacion completa es {resultado} = {suma}')



print()
#19 Escriu un programa que demani una frase a l’usuari i que compti i mostri el nombre de vegades que apareixen les vocals. 

frase = input("Introduce una frase: ")

vocales = "AEIOUaeiou"

vocal = 0
index = 0

while index < len(frase):
    if frase[index] in vocales:
        vocal += 1
    index +=1

print(f'En la frase {frase}, el numero de vocales que aparecen es de {vocal}')



