print("El siguiente programa realizara la suma de todos los numeros enteros entre el 0 y el 100")

numero1 = 0
numero2 = 100

numeroactual = numero1
suma = 0

while numeroactual <= numero2:
    suma += numeroactual
    numeroactual += 2

print(f'La suma de los numeros enteros entre {numero1} y {numero2} es de {suma}')

print()

frase = input('Escriu una frase d\'entrada: ')

listafrase = frase.split(' ')
contplabr = 0

while contplabr < len(listafrase):
    print(' '.join(listafrase[0:contplabr]))
    contplabr += 1
print(' '.join(listafrase))

contplabr -= 1
listafraseinv = listafrase[::-1]

while contplabr >= 0:
    print(' '.join(listafraseinv[0:contplabr]))
    contplabr -= 1

numerointro = int(input("Introduce un numero: "))
contador = 1
linea = 1

while linea <= 2*numerointro-1:
    numeroespacio = numerointro - contador
    if linea < numerointro:
        if linea%2 == 1:
            print(" "*numeroespacio+f'{contador}-'*(contador)+f'{contador}')
        else:
            print(" "*numeroespacio+f'{contador}*'*(contador)+f'{contador}')
        contador += 1
    elif linea >= numerointro:
        if linea%2 ==1:
           print(" "*numeroespacio+f'{contador}-'*(contador)+f'{contador}')
        else:
            print(" "*numeroespacio+f'{contador}*'*(contador)+f'{contador}')
        contador += 1
    linea += 1

print()
            