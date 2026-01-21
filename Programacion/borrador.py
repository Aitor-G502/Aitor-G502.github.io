#7


numobjetivo = int(input("Escribe un numero entero aqui: "))

num = 2

esprimo = True 

while numobjetivo >= num:
    if (numobjetivo %num == 0):
        esprimo = False
        break
    num += 1

