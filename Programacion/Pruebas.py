numimpar = int(input("Introduce un numero impar: "))



while numimpar % 2 == 0:
    numimpar = int(input("Ese numero no es impar, porfavor introduce otro numero impar: "))

print(f"Tu numero {numimpar} es un numero impar")





# 

frase = input("Introduce una frase: ")

listafrase = frase.split(" ")
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
