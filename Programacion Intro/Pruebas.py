# 1
frase = input("Escribe una frase: ")

listafrase = frase.split(' ')
contador = 0

while contador < len(listafrase):
    print(' '.join(listafrase[0:contador]))
    contador += 1
print(' '.join(listafrase))

contador -= 1

listafraseinv = listafrase[::-1]

while contador >= 0:
    print(' '.join(listafraseinv[0:contador]))
    contador -= 1



# 2 




