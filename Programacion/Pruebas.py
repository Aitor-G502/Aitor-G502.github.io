print("El siguiente programa realizara la suma de todos los numeros enteros entre el 0 y el 100")

numero1 = 0
numero2 = 100

numeroactual = numero1
suma = 0

while numeroactual <= numero2:
    suma += numeroactual
    numeroactual += 2

print(f'La suma de los numeros enteros entre {numero1} y {numero2} es de {suma}')