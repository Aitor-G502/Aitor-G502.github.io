numimpar = int(input("Introduce un numero impar: "))



while numimpar % 2 == 0:
    numimpar = int(input("Ese numero no es impar, porfavor introduce otro numero impar: "))

print(f"Tu numero {numimpar} es un numero impar")
