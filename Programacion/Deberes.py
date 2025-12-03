#Ejercicio 1: Crea un programa que determini si un número introduït des de teclat és positiu, negatiu o zero.
 
numero = int(input("Introduce un numero:"))
if numero > 0:
    print("Tu numero es positivo")
elif numero < 0:
    print("Tu numero es negativo")
else:
    print("Tu numero es cero")





#Ejercicio 2: Escriu un programa que escrigui per pantalla si una fruita es "cítrica", "dolça", "fruit sec" o "altra" 
#utilitzant entrada per teclat (utiliza una llista per cada tipus de fruita, conjunt o tupla per la comprovació).

listacitricos = ["Limon", "Naranja", "Mandarina", "Lima", "Pomelo"]
listadulces = ["Manzana", "Mango", "Pera", "Platano", "Uva"]
listafrutossecos = ["Cacauetes", "Pistachos", "Almendras", "Anacardos", "Avellanas"]
listaotros = ["Arandanos", "Frambuesas", "Papaya", "Maracuya", "Guayaba"]

fruta = input("Introduce tu fruta favorita:")

if fruta in listacitricos:
    print("Tu fruta favorita es citrica")

elif fruta in listadulces:
    print("Tu fruta favorita es dulce")

elif fruta in listafrutossecos:
    print("Tu fruta favorita no es una fruta, es un fruto seco")

elif fruta in listaotros:
    print("Tu fruta favorita es otro tipo, no es ni citrica, ni dulce ni es un fruto seco")

else:
    print("Esa fruta no esta en nuestras listas")


#Ejercicio 3:Crea un programa que determini si una persona té menys de 18 anys (menor), té més o igual a 18 anys 
# (si té entre 18 y 30 -inclosos- és un adult jove, si te entre 31 y 65 anys és un adult, si té més de 65 anys és un adult senior) 
# i m’imprimeixi per pantalla el tipus de persona.

edad = int(input("Introduce tu edad:"))

if edad < 18:
    print("Eres menor de edad, ¡SAL DE AQUI!")

elif edad >= 18 and edad <= 30:
    print("Eres un adulto joven")

elif edad >= 31 and edad <= 65:
    print("Eres un adulto")

elif edad > 65:
    print("Eres un adulto senior")


#Ejercicio 4:Creeu un programa que determini el dia de la setmana a partir d'un número de l'1 al 7 (1 Dilluns…i finalment 7 Diumenge).



dia = int(input("Introduce el dia de la semana en numeros del 1 al 7:"))

if dia == 1:
    print("Hoy es Lunes")

elif dia == 2:
    print("Hoy es Martes")

elif dia == 3:
    print("Hoy es Miercoles")

elif dia == 4:
    print("Hoy es Jueves")

elif dia == 5:
    print("Hoy es Viernes")

elif dia == 6:
    print("Hoy es Sabado")

elif dia == 7:
    print("Hoy es Domingo")

else:
    print("No existen mas dias en la semana")



#Ejercicio 5: Escriu un programa que classifiqui un animal en "mamífer", "au", "rèptil" o "un altre" .

listamamiferos = ["Leon", "Tigre", "Hiena", "Delfin", "Gato"]
listaaves = ["Paloma", "Gorrion", "Loro", "Cuervo", "Halcon", "Pingüino"]
listareptiles = ["Dragon de komodo", "Sargantana", "Serpiente", "Alligator", "Iguana"]


animal = input("Nombra a un animal:")

if animal in listamamiferos:
    print("El animal nombrado es un Mamifero")

elif animal in listaaves:
    print("El animal nombrado es un Ave")

elif animal in listareptiles:
    print("El animal nombrado es un reptil")

else:
    print("Tu animal no esta en nuestras listas")




#6 Creeu un programa que calculi el cost d'enviament d’un paquet segons la distància: fins a 10 km, 10-50 km, o més de 50 km.

Distancia = int(input("Distancia del paquete a tu casa en Km:"))

if (Distancia <= 10):
    print("Tu coste de envio se ha reducido un 25% ")

elif (Distancia >= 10) and (Distancia <= 50):
    print("Tu coste de envio se ha reducido al 50%")

elif (Distancia >= 50):
    print("¡Tu coste de envio ahora es GRATIS!")



#7 Crea un programa que assigni una qualificació a una nota numèrica (A, B, C, D o F) en funció d’una nota numérica donada per teclat 
# (A = entre 9 i 10 -ambdós inclosos-, B = entre 7 i 9 -incloent el 7 però no el 9- , C = entre 5 i 7 -incloent el 5 però no el 7-, F = menys de 5).


nota = int(input("Introduce tu nota:"))

if (nota <= 10) and (nota >= 9):
    print("Tienes una A")

elif (nota >=7) and (nota < 9):
    print("Tienes una B")

elif (nota >=5) and (nota < 7):
    print("Tienes una C")

elif (nota < 5):
    print("Tienes una F")

# 8 Escriu un programa que classifiqui un dia de la setmana a "laborable" o "cap de setmana".

semana = input("Escribe un dia de la semana:")

if (semana == "Lunes") or (semana == "Martes") or (semana == "Miercoles") or (semana == "Jueves") or (semana == "Viernes"):
    print("Hoy es un dia laborable")
elif (semana == "Sabado") or (semana == "Domingo"):
    print("Hoy es fin de semana")

# 9 Escriu un programa que emmagatzemi la cadena de caràcters contrasenya en una variable, 
# pregunteu a l'usuari per la contrasenya i imprimiu per pantalla si la contrasenya introduïda per l'usuari coincideix 
# amb la desada a la variable sense tenir en compte majúscules i minúscules.

contraseña = ("Hola123")

verificacion = input("Intoduce tu contraseña para verificar que eres tu:")

if (verificacion == contraseña):
    print("Contraseña correctamente verificada, eres tu")

elif (verificacion != contraseña):
    print("Contraseña incorrecta, ¡VAYASE DE AQUI!")


# 10 Escriu un programa que demani a l'usuari dos números i en mostri per pantalla la divisió. Si el divisor és zero, el programa ha de mostrar un error.

numero1 = int(input("Escriba el dividendo de la division:"))
numero2 = int(input("Escriba el divisor de la division:"))

if (numero2 == 0):
    print("FATAL ERROR, no se puede dividir entre 0")

else:
    print(f"El resultado de tu division es {numero1 / numero2}")


# 11 Per tributar un determinat impost cal ser major de 16 anys i tenir uns ingressos iguals o superiors a 1000 € mensuals. 
# Escriure un programa que pregunti a l’usuari la seva edat i els seus ingressos mensuals i mostri per pantalla si l’usuari ha de tributar o no.

edadusuario = int(input("Introduzca su edad:"))
salariousuario = int(input("Introduzca su salario:"))

if (edadusuario >= 16) and (salariousuario >= 1000):
    print("Tienes que tributar")

elif (edadusuario < 16) or (salariousuario < 1000):
    print("No tienes que tributar")



# 12 Els alumnes d'un curs s’han dividit en dos grups A i B d’acord amb el sexe i el nom.
#  El grup A està format per les dones amb un nom anterior a la M i els homes amb un nom posterior a la N i el grup B per la resta. 
# Escriu un programa que pregunti a l'usuari el nom i el sexe, i mostri per pantalla el grup que li correspon.

nombrealumno = input("Esciribe tu nombre:")
generoalumno = input("Introduce tu genero (Hombre o Mujer):")

if (nombrealumno < "M" ) and (generoalumno == "Mujer"):
    print("Perteneces al grupo A")
elif (nombrealumno > "N") and (generoalumno == "Hombre"):
    print("Perteneces al grupo A")

else:
    print("Perteneces al grupo B")

# 13 Escriu un programa que pregunti a l'usuari la renda anual i mostri per pantalla el tipus impositiu que li correspon.

rentaanual = int(input("Escribe tu renta anual:"))

if (rentaanual < 10000):
    print("Te corresponde un 5%")

elif (rentaanual >= 10000) and (rentaanual <= 20000):
    print("Te corresponde un 15%")

elif (rentaanual >= 20000) and (rentaanual <= 35000):
    print("Te corresponde un 20%")

elif (rentaanual >= 35000) and (rentaanual <= 60000):
    print("Te corresponde un 30%")

elif (rentaanual > 60000):
    print("Te corresponde un 45%")


# EJERCICIOS MATCH 

# 1 Implementa un programa que verifiqui si una fruita és "poma", "plàtan" o "una altra" utilitzant match.

frutamatch = input("Introduce tu fruta favorita:")

match frutamatch:
    case "Manzana":
        print("Es una Manzana")
    case "Platano":
        print("Es un Platano")
    case _:
        print("Es otra fruta que no encontramos")

# 2 Implementa una funció que determini el dia de la setmana a partir d'un número de l'1 al 7 fent servir match.

diassemana = int(input("Introduce el numero del dia de la semana (1-7):"))

match diassemana:
    case 1:
        print("Es Lunes")
    case 2:
        print("Es Martes")
    case 3:
        print("Es Miercoles")
    case 4:
        print("Es Jueves")
    case 5:
        print("Es Viernes")
    case 6:
        print("Es Sabado")
    case 7:
        print("Es Domingo")
    case _:
        print("No es ningun dia de la semana porque la semana solo tiene 7 dias")


# 3 Escriu un programa que rebi com a entrada (serà l'entrada per teclat) els codis: 200, 301, 302, 404, 500 i 503. 
# El significat d'aquests codis és el següent: 
# '200' = 'Tot ok', '301' = 'Moviment permanent de la pàgina', '302' = 'Moviment temporal de la pàgina', 
# '404' = 'Pàgina no trobada', '500' = 'Error intern del servidor', '503' = 'Servidor no disponible '. 
# El programa haurà de tornar el missatge corresponent al codi introduït. Si s'introdueix un codi no comprès entre aquests,
#  el programa ha de tornar per pantalla el missatge 'Missatge desconegut'. 
# Tot això ho hauràs de ver fent servir match.

codigos = int(input("Introduce tu codigo:"))

match codigos:
    case 200:
        print("Todo esta ok")
    case 301:
        print("Movimiento permanente de la pagina")
    case 302:
        print("Movimiento temporal de la pagina")
    case 404:
        print("Pagina no encontrada")
    case 500:
        print("Error interno del server")
    case 503:
        print("Server no disponible")
    case _:
        print("Mensaje desconocido")