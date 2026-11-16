# Nos devuelve un numero de lineas en base a un numero base introducido
def genNumOfLine(num: int , numIntro: int) -> int:
    ''' Generate a number of lines based on a number 
        
        Arg:
        - num = Number that we need to used to generate the lines
        - numIntro = Number the user put at the beginning of the program
    '''
    return numIntro - num + 1


def genNumsLine(num: int) -> int:
    ''' Generate the numbers of the line

        Arg:
        - num = Number the user put 
    '''