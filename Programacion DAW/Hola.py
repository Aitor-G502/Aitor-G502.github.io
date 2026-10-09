fruta_ver = input("Introduce el nombre de una fruta: ")

match fruta_ver:
    case 'manzana':
      print("Tu fruta es una manzana")
    case "platano":
      print('Tu fruta es un platano')
    case _:
        print("Tu fruta es otro tipo de fruta")
