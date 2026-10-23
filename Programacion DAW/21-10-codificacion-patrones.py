frase = input("Introduce una frase: ")
indice = 0
fase = frase.split()

while len(frase) >= indice:
    print(frase[indice])
    indice += 1

