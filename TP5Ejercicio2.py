################
# Maitena Rue - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def fibonacci(numero):
    serie = [1,1]
    for i in range(numero -2):
        serie.append(serie[-1] + serie[-2])

    n_esimo = serie[numero -1]                           
    return n_esimo


def prueba():
    numero = input('Ingrese un numero entero: ')
    numero = int(numero)
    
    print(fibonacci(numero))
    

if __name__ == "__main__":
    prueba()
        
