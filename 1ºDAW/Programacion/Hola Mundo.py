num_intr = int(input('Introduce un numero entero: '))
num_index = 1
patron= ''
while num_intr > num_index:
    patron += '* '*num_index +"\n"
    num_index += 1

lista_patron = patron.split('\n')
lista_patron.reverse()
print(f'{patron + '* '*num_intr +  '\n'.join(lista_patron)}')
    
    
print()