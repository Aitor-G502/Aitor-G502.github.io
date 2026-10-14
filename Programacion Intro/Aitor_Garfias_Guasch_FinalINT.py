''' 1er Exercici:
Realitza un programa que amb una entrada n = 5 realitzi el següent patró:

#
# ##
# ## ###
# ## ### #### 
# ## ### #### #####
2 punts.

'''

numero1 = int(input("Introduce un numero: "))
contador = 1

while contador <= numero1:
    print(contador*"# ")
    contador += 1



''' 2n Exercici:
Realitza un programa que amb una entrada n = 4 realitzi el següent patró:

@#$%
- - - -
@@##$$%%
- - -
@@@###$$$%%%
- -
@@@@####$$$$%%%%
-
2 punts
'''
numero2 = int(input("Introduce un numero: "))
contador = 1
numerocontador = numero2

while contador <= numero2:
    print(contador*"@#$%")
    print((numerocontador*"- "))
    numerocontador -= 1
    contador += 1
    
    
    





''' 3er Exercici
Realitza un programa que amb una entrada n = 5 realitzi el següent patró:
'

    1        
   2-2       
  3-3-3
 4-4-4-4
5-5*5-5*5
 4*4*4*4
  3*3*3
   2*2
    1

3 punts
'''
numero3 = int(input("Introduce un numero:"))

contador = 1
numerocontador = numero3 + contador
numerocontador2 = numero3


while contador <= numero3:
    print(" "*numerocontador, contador * str(contador), " "*numerocontador)
    numerocontador -= 1
    contador += 1
contador = numero3

while contador > 0:
    print(" "*numerocontador,  contador * str(contador), " "*numerocontador)
    contador -= 1
    numerocontador += 1






''' 4e Exercici
# Donat un número d’una xifra n = 5 y una palaula introduïa = holas, codifica una 
# aplicació que dibuixi el següent patró:

Holas ***** holAS **** HOLas *** hOLAS ** HOLAS *
holaS #### HOlas ### hoLAS ## HOLAs #
Holas *** holAS ** HOLas *
holaS ## HOlas #
Holas *
holaS ** HOlas *
Holas ### holAS ## HOLas #
holaS **** HOlas *** hoLAS ** HOLAs *
Holas ##### holAS ##### HOLas ### hOLAS ## HOLAS #

3 punts
'''


