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

