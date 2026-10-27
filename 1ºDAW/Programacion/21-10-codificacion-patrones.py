''' 2º
frase = input("Introduce una frase: ")
indice = 0
fase = frase.split()

while len(fase) > indice:
    print(fase[indice])
    indice += 1
'''

''' 3º
1 - 
* * * *
2 - 22 -
* * *
3 - 33 - 333 -
* *
4 - 44 - 444 - 4444 -
* *
3 - 33 - 333 -
* * *
2 - 22 -
* * * *
1 - 

'''

numero = int(input("Introduce un numero entero: "))
indice = 1
num = numero

while numero >= indice:
    if indice > 1:
        print(f'{str(indice)} - {str(indice) * indice} -  ')
    else:
        print(f'{indice} - ')
    indice += 1
    if num > 2:
        print(f'{(num *'* ')} ')
    else:
        print(f'{(num *'* ')} ')
        num -= 1
    num -= 1



    
    
    
