'''
Mientras no se reciba como entrada al input un 1, 2, 3 o 4 se seguira pidiendo una entrada correcta indicando que la entrada anterior no lo era
'''

opcion = int(input('Introduce un numero del 1 al 4: '))

while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
    opcion = int(input("Introduce otra vez un numero del 1 al 4, que al parecer no sabes los numeros: "))
print('Muy bien te sabes los numeros del 1 al 4')


lista3 = [[1,3], [3,4], ['hola','tres'], ['5',5], [1, 2, 'janders']]
indice = 0
while indice <= (len(lista3) - 1):
    print(f'El siguiente elemento de la lista3 es: {lista3[indice]}')
    indelem = 0
    while indelem <= (len(lista3[indice]) - 1):
        print(f'El primer elemento de la sublista {lista3[indice]} es: {lista3[indice][indelem]}')
        indelem += 1
    indice += 1 

# Escriurem la sortida dels bucles anteriors d'aquesta manera:

'''
- Iteración bucle principal 1:
    Escribira por pantalla el primer indice de la lista 
        . [1,3]
    - Iteración bucle interno 1:
        Escribira por pantalla el primer objeto de la lista principal y despues los objetos de la sublista
            . [1, 3]
            . 1
            . [1, 3]
            . 3
        Despues se aumenta el indice +1 y el segundo indice +1
        Y volvemos a empezar
- Iteracion bucle princial 2:
    Escribira por pantalla el segundo objeto de la lista principal
        . [3,4]
        -Iteracion bucle interno 2:
        Escribira por pantalla el segundo objeto de la lista principal y despues los objetos de la sublista
        . [3,4] 
        . 3
        . [3, 4]
        . 4
        Despues se aumenta el indice +1 y el segundo indice +1
        Y volvemos a empezar
-Iteracion bucle principal 3:
    Escribe por pantalla el tercer objeto de la lista principal
        . ['hola', 'tres']
    -Iteracion bucle interno 3:
        Escribe por pantalla el tercer objeto de la lista principal y despues los objetos de la sublista
            . ['hola','tres']
            . hola
            . ['hola','tres']
            . tres
'''