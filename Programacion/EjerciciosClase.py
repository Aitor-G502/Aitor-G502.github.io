# Feu un bucle que realitzi el següent patro:
#EN el cas d'introdüir un nombre n = 4 y una paraula = "hola" tendria la seguent forma:
# hola
# hola hola
# hola hola hola
# hola hola hola hola
# aloh aloh aloh
# aloh aloh
# aloh

n = int(input("Introduce un numero: "))

palabra = input("Escribe una palabra: ")

palabrainv = list(palabra)
palabrainv = palabrainv[::-1]
palabrainv = ''.join((palabrainv))

numLin = 1

while numLin <= 2*n - 1:
    if numLin <= n:
        print((palabra + ' ')*numLin)
    else:
        print((palabrainv + ' ')*(2*n - numLin))
    numLin = numLin + 1