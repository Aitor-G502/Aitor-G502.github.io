# 2 Imagina que te han dado la frase = 'Hola como vas amigo mío.'

frase = input("Introduce una frase: ").split()


contador = 0
contador2 = 0
fraseinv = frase[::-1]

while contador < len(frase):
    print(" ".join(frase[:contador+1]))
    contador += 1

while contador2 < len(fraseinv):
    print(" ".join(frase[contador2:]))
    contador2 += 1