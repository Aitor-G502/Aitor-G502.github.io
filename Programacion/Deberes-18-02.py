# 2 Imagina que te han dado la frase = 'Hola como vas amigo mío.'

frase = input("Introduce una frase: ").split()


contador = 0
contador2 = 0
fraseinv = frase[::-1]

while contador < len(frase):
    print(" ".join(frase[:contador+1]))
    contador += 1

while contador2 < len(fraseinv):
    print(" ".join(fraseinv[::contador2+1]))
    contador2 += 1


#3 

num = int(input("Introduce la cantidad del patron: "))

numcontador = 1

numlinea = ""

while num > numcontador: 
    print(numcontador)
    print("*"*numcontador)
    numcontador += 1


