listaejemplo = [15, 12, 34, 56, 12, 12, 3, 4, 6, 5, 7, 8]

#1 - Imprime por pantalla cuantas veces aparece el numero 12

print(f"En la lista el numero 12 aparece: {listaejemplo.count(12)}")

#2 - Inserta un mumero leido por teclado en la posicion 4 de la lista(indice 3)

numero_usuario = int(input("Intoduce un numero para insertar en la posicon 4: "))
listaejemplo.insert(3,numero_usuario)
print(f"La lista con el nuevo numero insertado en la posicion 4: {listaejemplo}")

#3 - Imprime la lista con los elementos invertidos de posicion

listaejemplo.reverse()
print(f"La lista con los elementos invertidos de posicion: {listaejemplo}")

#4 - Tienes otra lista: [1, 2, 3] añadela como unico elemento al final de listaejemplo

listaejemplo2 = [1, 2, 3]
listaejemplo.append(listaejemplo2)
print(f"La lista listaejemplo con la  lista listaejemplo2 añadida como un unico elemento queda: {listaejemplo}")

#5 - Extiende la lista listaejemplo con los elementos de la lista del punto anterior

listaejemplo.extend(listaejemplo2)
print(f"La lista listaejemplo con la  lista listaejemplo2 extendida queda : {listaejemplo}")

#6 - Extrae el elemento 12 de la lista (una vez) y imprime como queda la lista despues de extraerlo

listaejemplo.remove(12)
print(f"La lista con el primer 12 que encontró extraido queda: {listaejemplo}")

#Ejercicio rapido:
#Crea una lista que tenga 3 dimensiones en las que cada sublista contenga almenos 3 elementos
#Quiero que imprimais el 3er elemento de la lista que esta dentro del 3er elemento de la lista
#que se encuentra en la 3ª posicion de la lista principal 'listratri

print()
print()
listatri = [[[1, 2, 3], [4, 5, 6], [8, 9, 10]], [[11, 12, 13], [14, 15, 16], [18, 19, 20]], [[21, 22, 23], [24, 25, 26], [28, 29, 30]]]
print(f"El tercer elemento de la lista que esta dentro del tercer elemeto de la lista que se encuentra en 3ª posicion de la lista principal es: {listatri[2][2][2]}")
