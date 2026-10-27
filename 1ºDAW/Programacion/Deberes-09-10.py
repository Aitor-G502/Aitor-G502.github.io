'''
Un programa para saber si puedes optar por una beca o no y cuanto te toca
'''
casa = int(input("Vives en la casa de tus padres (1) o vives por tu cuenta (2): "))

trabajo = input('Usted trabaja o estudia(solo responda con "trabajo" en caso de que trabaje y "estudio" en caso de que estudie): ')

if casa == 1:
    padres = input('Tus padres estan divorciodos?(si o no): ')
    if padres == 'si' and trabajo == 'trabajo':
        print(f'Tienes derecho a una beca, y su resolucion podra llegar a los 1000€')
    elif padres == 'no' and trabajo == 'estudio':
        salario_padres = int(input("cual es el salario anual de tus dos padres en total?: "))
        if salario_padres < 20000:
            print(f'Tienes derecho a una beca que su resolucion puede llegar a 1700€')
        else:
            print(f'No puedes solicitar la beca')
    elif padres == 'no' and trabajo == 'trabajo':
        print('No puedes solicitar la beca')
    elif padres == 'si' and trabajo == 'estudio':
        salario_padres = int(input('cual es el salario de tu padre/madre?: '))
        if salario_padres <10000:
            print('Tienes derecho a solicitar la beca y su resolucion puede llegar a 1700€')
        elif salario_padres < 20000:
            print("Tienes derecho a solicitar la beca y su resolucion puede llegar a 1200€")
        else:
            print('No puedes solicitar la beca')
elif casa == 2:
    if trabajo == 'trabajo':
        salario = int(input('cual es tu salario anual?: '))
        if salario < 10000:
            print('Tienes derecho a solicitar la beca y su resolucion puede llegar a 1500€')
        elif salario < 15000:
            print('Tienes derecho a solicitar la beca y su resolucion puede llegar a 1000€')
        else:
            print('No puedes solicitar la beca')
    elif trabajo == 'estudio':
        print('Tienes derecho a solicitar la beca y su resolucion puede llegar a 1700€') 

'''
Un programa para saber si puedes solicitar el paro
'''

dias_trabajado = int(input('Cuantos dias has trabajado?: '))

if dias_trabajado < 359:
    print('No puede solicitar el paro')
elif dias_trabajado < 540:
    print('Tienes derecho a 4 meses de paro (120 dias)')
elif dias_trabajado >= 720 and dias_trabajado < 900:
    print('Tienes derecho a 8 meses de paro (240 dias)')
elif dias_trabajado >= 1080 and dias_trabajado <1260:
    print("Tienes derecho a 12 meses de paro (360 dias)")
elif dias_trabajado > 2160:
    print('Tienes derecho a 24 meses de paro (720 dias)')