'''
Acceso a discoteca
Variables: edad:int, dni_valido:bool, en_lista_negra:bool
Pide: ¿Puede entrar? (edad sea mayor o igual que 18, el DNI sea válido y no esté en lista negra)
'''
edad1 = 18
dni_valido1 = True
en_lista_negra1 = False

edad2 = 16
dni_valido2 = True
en_lista_negra2 = False

edad3 = 65
dni_valido3 = False
en_lista_negra3 = True

print("¿Puede entrar el primero?")
print((edad1 >= 18) and dni_valido1 == True and not en_lista_negra1 )
print()
print("¿Puede entrar el segundo?")
print((edad2 >= 18) and dni_valido2 == True and not en_lista_negra2)
print()
print("¿Puede entrar el tercero?")
print((edad3 >= 18) and dni_valido3 == True and not en_lista_negra3)
print()

'''
Envío gratis en tienda online
Variables: importe_pedido:float, es_premium:bool
Pide: ¿Tiene envío gratis? (importe del pedido sea mayor o igual que 50 euros o el cliente sea premium)
'''
importe_pedido1 = 56.50
es_premium1 = True

importe_pedido2 = 36.75
es_premium2 = True

importe_pedido3 = 26.68
es_premium3 = False

print("¿Tiene la primera persona el envío gratis?")
print((importe_pedido1 >= 50) or es_premium1 == True)
print()
print("¿Tiene la segunda persona el envío gratis?")
print((importe_pedido2 >= 50) or es_premium2 == True)
print()
print("¿Tiene la tercera persona el envío gratis?")
print((importe_pedido3 >= 50) or es_premium3 == True)
print()

'''
Renovación de carnet
Variables: edad:int, puntos:int
Pide: ¿Puede renovar? (edad sea mayor o igual que 18 y al mismo tiempo sea menor o igual que 65, y los puntos sean mayores o iguales que 8)
'''

edad1 = 18
edad2 = 65
edad3 = 75

puntos1 = 8
puntos2 = 15
puntos3 = 3

print("¿Puede la primera persona renoverse el carnet?")
print((edad1 >= 18 and edad1 <= 65) and puntos1 >=8)
print()
print("¿Puede la segunda persona renoverse el carnet?")
print((edad2 >= 18 and edad2 <= 65) and puntos2 >=8)
print()
print("¿Puede la tercera persona renoverse el carnet?")
print((edad3 >= 18 and edad3 <= 65) and puntos3 >=8)
print()

'''
Aprobado con recuperación
Variables: nota_final:float, nota_examen:float, trabajo_entregado:bool
Pide: ¿Aprueba? (la nota final sea mayor o igual que 5, o bien que la nota del examen sea mayor o igual que 4 y el trabajo haya sido entregado)
'''

nota_final1 = 4.7
nota_examen1 = 4.0
trabajo_entregado1 = True