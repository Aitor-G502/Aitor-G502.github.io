'''
1 # 7 ## 7 ### 7 #### 7 ##### 7 ###### 7 ####### 7
2 # 2 ## 6 ### 6 #### 6 ##### 6 ###### 6 ##### 6
3 # 3 ## 3 ### 5 #### 5 ##### 5 #### 5 ### 5
4 # 4 ## 4 ### 4 #### 4 ### 4 ## 4 # 4
5 # 5 ## 5 ### 5 ## 5 # 3 ## 3 ### 3
6 # 6 ## 6 # 6 ## 6 # 6 ## 2 # 2
7 # 7 # 7 # 7 # 7 # 7 # 7 # 1

'''
numero = int(input("Introduce un numero entero: "))
indice = 1

while indice <= numero:
    linea = str(indice)
    i = numero
    while i >= 1:
        linea = linea + " " + "#" * i + " " + str(numero)
        i -= 1
        
    print(linea)
    indice += 1