#list.append() #añade un nuevo dato al final de una lista 

numeros = [1, 2, 3]
numeros.append([4,5])
print(numeros)

#list.clear()  #elimina todos los elementos de una lista

numeros2 = [1, 2, 3]
numeros2.clear()
print(numeros2)

#list.count() # cuenta las veces que aperece un elemento X dentro de una lista

numeros3 = [1, 2, 2, 3, 3, 2, 5, 2]
print(numeros3.count(2))

#list.extend() #añade nuevos elementos uno por uno desde otra lista

numeros4 = [1, 2, 3]
numeros4.extend([4, 5, 6])
print(numeros4)

#list.insert() #añade un elemento en una posicion especifica sin eliminar a los que ya estan en la lista

numeros5 = [1, 2, 4, 5, 6, 7]
numeros5.insert(2, 3)
print(numeros5)

#list.remove() #elimina la primera aparicion de un elemento X

numeros6 = [1, 2, 3, 4, 3, 5, 6]
numeros6.remove(3)
print(numeros6)

#list.reverse() #Invierte los elementos de una lista

numeros7 = [8, 7, 6, 5, 4, 3, 2, 1]
numeros7.reverse()
print(numeros7)