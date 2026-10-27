''' 1º
Crea un programa que determini si un número introduït des de teclat és positiu, negatiu o zero.
'''
num = float(input("Introduce un numero: "))


if num < 0:
   print(f'{num} es un numero negativo')
elif num == 0:
   print(f'{num} es zero')
else:
   print(f'{num} es un numero positivo')


''' 2º
Escriu un programa que escrigui per pantalla si una fruita es
"cítrica", "dolça", "fruit sec" o "altra" utilitzant entrada per teclat
(utiliza una llista per cada tipus de fruita, conjunt o tupla per la comprovació).
'''

citrica = ['limon', 'naranja', 'pomelo', 'lima', 'mandarina']
dulce = ['fresa', 'platano', 'uva', 'mango', 'manzana']
fruto_seco =  ['cacahuete', 'pistacho', 'quico', 'pasas']



fruta = input("Introduce tu fruta favorita: ")


if fruta == citrica[0] or fruta == citrica[1] or fruta == citrica[2] or fruta == citrica[3] or fruta == citrica[4]:
   print(f'{fruta} es un citrico')
elif fruta == dulce[0] or fruta == dulce[1] or fruta == dulce[2] or fruta == dulce[3] or fruta == dulce[4]:
   print(f'{fruta} es una fruta dulce')
elif fruta == fruto_seco[0] or fruta == fruto_seco[1] or fruta == fruto_seco[2]:
   print(f'{fruta} es un fruto seco')
else:
   print(f'{fruta} es otro tipo de fruta diferente')


''' 3º
Crea un programa que determini si una persona té menys de 18 anys (menor),
té més o igual a 18 anys (si té entre 18 y 30 -inclosos- és un adult jove,
si te entre 31 y 65 anys és un adult, si té més de 65 anys és un adult senior)
i m’imprimeixi per pantalla el tipus de persona.


'''
edad = int(input('Introduce tu edad: '))


if edad <0:
   print(f'Introduce un numero valido')
elif edad <18:
   print(f'Eres menor de edad')
elif edad >=18 and edad <= 30:
   print(f'Eres un adulto joven')
elif edad >31 and edad <= 65:
   print(f'Eres un adulto')
else:
   print(f'Eres un adulto senior')


''' 4º
Creeu un programa que determini el dia de la setmana a partir d'un número de l'1 al 7 (
1 Dilluns…i finalment 7 Diumenge).
'''


semana_menu = ''' 1 - Lunes
2 - Martes
3 - Miercoles
4 - Jueves
5 - Viernes
6 - Sabado
7 - Domingo


'''
semana_dia = 'Hoy es'


semana_menu_sel = int(input(semana_menu))
match semana_menu_sel:
   case 1:
       print(f'{semana_dia} lunes')
   case 2:
       print(f'{semana_dia} martes')
   case 3:
       print(f'{semana_dia} miercoles')
   case 4:
       print(f'{semana_dia} jueves')
   case 5:
       print(f'{semana_dia} viernes')
   case 6:
       print(f'{semana_dia} sabado')
   case 7:
       print(f'{semana_dia} domingo')


''' 5º
Escriu un programa que classifiqui un animal en "mamífer", "au", "rèptil" o "un altre"
'''
mamifero = ['leon', 'gato', 'tigre', 'perro']
ave = ['paloma', 'loro', 'pato', 'Buho']
reptil = ['tortuga', 'iguana', 'dragon de komodo', 'serpiente']


animal = input("Escribe el nombre de tu animal favorito: ")


if animal == mamifero[0] or animal == mamifero[1] or animal == mamifero[2] or animal == mamifero[3]:
   print(f'{animal} es un mamifero')
elif animal == ave[0] or animal == ave[1] or animal == ave[2]  or animal == ave[3]:
   print(f'{animal} es un ave')
elif animal == reptil[0] or animal == reptil[1] or animal == reptil[2] or animal == reptil[3]:
   print(f'{animal} es un reptil')
else:
   print(f'Tu animal es otro tipo de animal que no esta registrado en nuestros datos')




''' 6º
Creeu un programa que calculi el cost d'enviament d’un paquet segons la distància: fins a 10 km, 10-50 km, o més de 50 km.
'''
distancia = float(input("Introduce la distancia en Km:"))


if distancia <= 10:
   print("No se cobrara coste de envio")
elif distancia  > 10 and distancia <=50:
   print("El coste de envio es de 5 euros")
else:
   print('El coste de envio es de 15 euros')


''' 7º
Crea un programa que assigni una qualificació a una nota numèrica (A, B, C, D o F)
en funció d’una nota numérica donada per teclat
(A = entre 9 i 10 -ambdós inclosos-, B = entre 7 i 9 -incloent el 7 però no el 9- , C = entre 5 i 7 -incloent el 5 però no el 7-, F = menys de 5).


'''


nota = int(input('Introduce tu nota: '))


if nota >= 9:
   print(f'Tienes una A')
elif nota >=7 and nota <= 8:
   print(f'Tienes una B')
elif nota >=5 and nota <= 6:
   print(f'Tienes una C')
else:
   print(f'Tienes una F')


''' 8º
Escriu un programa que classifiqui un dia de la setmana a "laborable" o "cap de setmana".
'''


semana = input('Escribe un dia de la semana: ')


if semana == 'Lunes' or semana == 'Martes' or semana == 'Miercoles' or semana == 'Juves' or semana == 'Viernes':
   print("Hoy es un dia laborable")
elif semana == 'Sabado' or semana == 'Domingo':
   print("Es fin de semana")
else:
   print("Eso no es un dia de la semana")


''' 9º
Escriu un programa que emmagatzemi la cadena de caràcters contrasenya en una variable,
pregunteu a l'usuari per la contrasenya i imprimiu per pantalla si la contrasenya introduïda per l'usuari coincideix
amb la desada a la variable sense tenir en compte majúscules i minúscules


'''
contraseña = ('contraseña')


preguntar_contr = input('Introduce la contraseña: ')


if preguntar_contr == contraseña:
   print("La contraseña coincide, bienvenido!")
else:
   print('La contraseña no coincide, vuelve a intentarlo')


''' 10º
Escriu un programa que demani a l'usuari dos números i en mostri per pantalla la divisió. Si el divisor és zero, el programa ha de mostrar un error.
'''
num_1 = float(input("Introduce el primer numero de la division:"))
num_2 = float(input("Introduce el segundo numero de la division:"))


if num_2 == 0:
   print("No se puede dividir entre 0")
else:
   print(f'La division entre {num_1} y {num_2} es {num_1/num_2}')


''' 11º
Per tributar un determinat impost cal ser major de 16 anys i tenir uns ingressos iguals o superiors a 1000 € mensuals.
Escriure un programa que pregunti a l’usuari la seva edat i els seus ingressos mensuals i mostri per pantalla si l’usuari ha de tributar o no.




'''
edad_usuario = int(input('Introduce tu edad: '))
ingresos_usuario = float(input("Introduce tus ingresos mensuales: "))


if edad_usuario >= 16 and ingresos_usuario >= 1000:
   print('Tienes que tributar')
else:
   print('No tienes que tributar')


''' 12º
Els alumnes d'un curs s’han dividit en dos grups A i B d’acord amb el sexe i el nom.
El grup A està format per les dones amb un nom anterior a la M i els homes amb un nom posterior a la N i el grup B per la resta.
Escriu un programa que pregunti a l'usuari el nom i el sexe, i mostri per pantalla el grup que li correspon.


'''
nombre = input("Escribe tu nombre aqui: ")
genero = input("Escribe aqui tu genero (hombre o mujer): ")


if genero == 'mujer' or genero == 'Mujer' and nombre < 'M':
   print("Perteneces al grupo A")
elif genero == 'hombre' or genero == 'Hombre' and nombre > 'N':
   print('Perteneces al grupo A')
else:
   print("Perteneces al grupo B")




''' 13º
Escriu un programa que pregunti a l'usuari la renda anual i mostri per pantalla el tipus impositiu que li correspon.


'''
renta = float(input("Introduce tu renta anual: "))


if renta < 10000:
   print(f'Tu renta es de {renta * 0.05}')
elif renta < 20000:
   print(f'Tu renta es de {renta * 0.15}')
elif renta < 35000:
   print(f'Tu renta es de {renta * 0.20}')
elif renta < 60000:
   print(f'Tu renta es de {renta * 0.30}')
else:
   print(f'Tu renta es de {renta * 0.45}')


''' 1º match
Implementa un programa que verifiqui si una fruita és "poma", "plàtan" o "una altra"
'''



fruta_ver = input("Introduce el nombre de una fruta: ")


match fruta_ver:
    case 'manzana':
      print("Tu fruta es una manzana")
    case "platano":
      print('Tu fruta es un platano')
    case _:
        print("Tu fruta es otro tipo de fruta")


''' 2º match
Implementa una funció que determini el dia de la setmana a partir d'un número de l'1 al 7


'''
dia_semana = int(input("Introduce el numero del dia de la semana (1-7): "))


match dia_semana:
    case 1:
      print(" Hoy es lunes")
    case 2:
      print("Hoy es martes")
    case 3:
      print("Hoy es miercoles")
    case 4:
      print("Hoy es jueves")
    case 5:
      print("Hoy es viernes")
    case 6:
      print("Hoy es sabado")
    case 7:
      print("Hoy es domingo")
    case _:
      print("Introduce un numero valido")


''' 3º match
Escriu un programa que rebi com a entrada (serà l'entrada per teclat) els codis:
200, 301, 302, 404, 500 i 503.
El significat d'aquests codis és el següent: '200' = 'Tot ok', '301' = 'Moviment permanent de la pàgina',
'302' = 'Moviment temporal de la pàgina', '404' = 'Pàgina no trobada', '500' = 'Error intern del servidor',
'503' = 'Servidor no disponible '. El programa haurà de tornar el missatge corresponent al codi introduït.
Si s'introdueix un codi no comprès entre aquests, el programa ha de tornar per pantalla el missatge 'Missatge desconegut'
'''


codigo = int(input("Introduce un codigo numerico: "))


match codigo:
    case 200:
      print("Todo ok")
    case 301:
      print("Movimiento permantente de la pagina")
    case 302:
      print("Movimiento temporal de la pagina")
    case 404:
      print("Pagina no encontrada")
    case 500:
      print("Error interno del servidor")
    case 503:
      print("Servidor no disponible")
    case _:
      print('Mensaje desconocido')

