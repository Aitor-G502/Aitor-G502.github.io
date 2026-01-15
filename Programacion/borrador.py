deberes = input("Escribe tu cadena de caracteres: ")

listadeberes = list(deberes)

nuevadeberes = []

ñ = 1

palabradeberes = ""

for letradeberes in listadeberes:
    if ñ %2 == 0:
        nuevadeberes.append(letradeberes.lower())
    else:
        nuevadeberes.append(letradeberes.upper())
    ñ = ñ+1

for letradeberes2 in nuevadeberes:
    palabradeberes = palabradeberes + letradeberes2

print(f'{palabradeberes}')
