'''
Jander
Jander JAnder
Jander JAnder JANder
Jander JAnder JANder JANDer
Jander JAnder JANder JANDer JANDEr
Jander JAnder JANder JANDer JANDEr JANDER
Jander JAnder JANder JANDer JANDEr JANDER JANDER
jandeR jandER janDER jaNDER jANDER JANDER
jandeR jandER janDER jaNDER jANDER
jandeR jandER janDER jaNDER
jandeR jandER janDER
jandeR jandER
jandeR
'''

palabra = input("Escribe una palabra: ")
numero = int(input("Introduce un numero entero: "))
salto = " "
index = 0
palabra.split()
print(palabra[index])

while numero >= index:
    print((palabra.upper() + salto) * index)
    index += 1

index = numero - 1

while index >= 1:
    print((palabra.upper() + salto) * index)
    index -= 1


