################
# Maitena Rue - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numeros_perfectos(numero):
    i = 2
    suma = 1                
    while numero > i :
        if numero % i == 0:       
            suma += i      
        i += 1    
     
    if (suma == numero) and (numero != 1):
        return True
    else:
        return False
    

def prueba():
    numero = input('Ingrese un numero entero positivo: ')
    numero = int(numero)
    
    num = numeros_perfectos(numero)
    if num == True:
        print('Es perfecto')
    else:
        print('No es perfecto')
        

if __name__ == "__main__":
    prueba()
