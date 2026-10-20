numero_entero = int(input("Introduce un numero entero: "))
divisor = 1
indice = 0

while numero_entero >= indice:
    if numero_entero % divisor == 0:
        print(f'{divisor} es divisor de {numero_entero}')
    divisor += 1
    indice += 1

