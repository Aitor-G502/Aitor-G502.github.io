nument = int(input("Introduce un numero entero entre el 0 y el 9: "))

listanument = [1, 3, 6, 9]

while True:
    match nument:
       case 2:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 4:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 5:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 7:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case 8:
            print("No has conseguido acertar un numero dentro de la lista")
            print(nument)
       case _:
            print("Enhorabuena, has conseguido acertar un numero en la lista")
            break
    print()
    nument = int(input("Introduce un numero entero entre el 0 y el 9: "))
