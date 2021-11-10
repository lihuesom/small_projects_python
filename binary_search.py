# Para una busqueda binaria se necesita la lista ya ordenada
# Si se desea optimizar el tiempo se requiere mas espacio en memoria 
# Si se desea utilizar menos memoria el algoritmo tardara aun mas

import random

contador = 0 #Crear un contador de iteraciones

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}') #Siempre que se accede por indice
    # si hay un len se debe restar 1
    global contador
    contador +=1

    if comienzo > final: #Si nuestro indice ya es mas grande que el final, ya no se encuentra en la lista
        return False

    medio = (comienzo + final) // 2 # partir la lista por la mitad realizando la division de enteros //

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)]) #Sorted ordena la lista

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo) #Se generan indices para moverse en la lista

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Se realizaron {contador} iteraciones')