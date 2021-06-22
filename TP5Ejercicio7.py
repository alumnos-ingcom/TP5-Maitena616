################
# Maitena Rue - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(n1, n2):
    centro = (n1 + n2) / 2
    radio = (n2 - n1) / 2
    
    if radio < 0:
        distancia = radio * -2
    else:
        distancia = radio * 2
    
    return distancia

def prueba():
    print('Ingrese dos numeros para conocer la distancia')
    n1 = input('Numero 1: ')
    n1 = float(n1)
    
    n2 = input('Numero 2: ')
    n2 = float(n2)
    
    dist = distancia(n1, n2)
    print(f'La distancia es: {dist}')
    
    
if __name__ == "__main__":
    prueba()
