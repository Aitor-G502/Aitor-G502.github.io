#10 Crea un programa que demani un text per teclat i que la sortida sigui el text invertit. No podrás fer servir la sintaxi [::-1]

texto = input("Escribe un texto aqui: ")

textoinv = len(texto) - 1

inv = ""

while textoinv >= 0:
    inv += texto[textoinv]
    textoinv -= 1
print(f'Tu texto invertido es: {inv}')





# 11  Imprimeix el següent patró utilitzant el bucle for, les dimensions del patró dependran d’un nombre introduït per teclat, 
# en el cas següent es mostra el patró si el nombre introduït és el 5:

num = int(input("Introduce un numero entero: "))

n = 1 


while n <=  2*num-1:
    if n <= num:
        print("* " *n)
    else:
        print("* " * (2*num-n))
    n += 1




    


# 12 Crea un programa utilitzant el bucle for que compti el nombre de xifres que té un número sencer introduït per teclat.

nument = input("Introduce un numero entero: ")

contador = 1

while contador < len(nument):
    contador = contador + 1

print(f'El numero tiene {contador} cifras')


#13 Escriu un programa que pregunti quants números s'introduiran, demaneu aquests números,
#  i mostri un missatge cada vegada que un nombre no sigui més gran que el primer nombre introduït.

cuantosnum = int(input("Cuantos numeros se introduciras: "))

demnum = int(input(f'Introduce {cuantosnum} numeros: '))


