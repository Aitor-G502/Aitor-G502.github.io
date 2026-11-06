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
mayus = 1

while numero >= index:
    print((palabra + salto) * index)
    index += 1

index = numero - 1

while index >= 1:
    print((palabra + salto) * index)
    index -= 1