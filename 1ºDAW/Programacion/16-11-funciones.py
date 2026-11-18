''' 1º
1 # 7 ## 7 ### 7 #### 7 ##### 7 ###### 7 ####### 7
2 # 2 ## 6 ### 6 #### 6 ##### 6 ###### 6 ##### 6
3 # 3 ## 3 ### 5 #### 5 ##### 5 #### 5 ### 5
4 # 4 ## 4 ### 4 #### 4 ### 4 ## 4 # 4
5 # 5 ## 5 ### 5 ## 5 # 3 ## 3 ### 3
6 # 6 ## 6 # 6 ## 6 # 6 ## 2 # 2
7 # 7 # 7 # 7 # 7 # 7 # 7 # 1

'''

# Nos devuelve el segundo numero del patron
def genSecondNum(num: int , numIntro: int) -> int:
    ''' Generate a number of lines based on a number 
        
        Arg:
        - num = Number that we need to used to generate the lines
        - numIntro = Number the user put at the beginning of the program
    '''
    return numIntro - num + 1

print(genSecondNum(1, 7))

# Nos devuelve una linea de numeros introducidos
def genNumsLine(num: int , num2: int) -> str:
    ''' Generate the numbers of the line

        Arg:
        - num = First number the program revieves 
        - num2 = Second number the program recieves
    '''  
    primero = ((str(num) + " ") * num)
    segundo = ((str(num2) + " ") * num2)
    
    return (primero + segundo).split()

print(genNumsLine(1, 7))

# Nos devuelve un caracter de relleno por un numero introducido
def genSingleFill(num: int) -> str:
    ''' Generate a single filler

    Arg:
    - num = Number recieved from the user
    
    '''
    return  num * '#'


print(genSingleFill(7))

def genFillerLine(num: int) -> str:
    ''' Generate the fillers line
    
    Arg:
    - num = Number revieved from the user
    '''
    return num * genSingleFill(num)

print(genFillerLine(7))


