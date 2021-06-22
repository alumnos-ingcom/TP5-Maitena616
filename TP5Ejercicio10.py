################
# Maitena Rue - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def binario(num):
    en_binario = []
    
    if num == 0:
        en_binario = ['0']
        
    while num >= 1:
        resto = num % 2
        resto = str(resto)
        en_binario.insert(0, resto)    
        num //= 2
            
    entero_en_binario = "".join(en_binario)
    return entero_en_binario


def entero(numero):
    suma = 0
    numero = numero.replace(" ", "")
    
    potencias = (len(numero)) -1      
    largo = len(numero)
    
    for i in range(largo):
        num = int(numero[i])  
        convertir = num * (2 **(potencias - i))
        suma += convertir
    
    return suma


def prueba():
    num = input('Ingrese un numero entero positivo: ')
    num = int(num)
    binarioN= binario(num)
    print(f'Su numero en binario es: {binarioN}')
    numero = input('\nIngrese un numero en binario: ')
    enteroN = entero(numero)
    print(f'Su numero decimal es: {enteroN}')


if __name__ == "__main__":
    prueba()
