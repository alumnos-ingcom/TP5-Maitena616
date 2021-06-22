################
# Maitena Rue - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comparar_listas(lista_1, lista_2):
    coincidencias = 0
    
    for i in range (len(lista_1)):
        for j in range (len(lista_1)):   
            if lista_1[i] == lista_2[j]:
                coincidencias += 1
    return coincidencias == len(lista_1)
       

def prueba():
    lista_1 = []
    lista_2 = []
    cantidad_de_numeros= input('Cuantos elementos tendran sus 2 listas: ')
    cantidad_de_numeros = int(cantidad_de_numeros)
    
    for i in range(cantidad_de_numeros):
        elemento_lista_1 = input(f'Elemento {i+1} de a lista (1): ')
        lista_1.append(elemento_lista_1)   
    for i in range(cantidad_de_numeros):
        elemento_lista_2 = input(f'Elemento {i+1} de a lista (2): ')
        lista_2.append(elemento_lista_2)
    
    resultado = comparar_listas(lista_1, lista_2)
    if resultado == True:
        print('Son iguales')
    else:
        print('No son iguales')
    
    
if __name__ == "__main__":
    prueba()
