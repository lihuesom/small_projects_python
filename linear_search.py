import random #Genera número aleatorios
contador = 0 

def busqueda_lineal(lista, objetivo): #
    match = False # Un solo elemento O(1)

    global contador
    contador += 1

    for elemento in lista: # Un bucle a lo largo de la lista O(n)
        if elemento == objetivo: #Comparacion 
            match = True #Una asignacion 
            break #Saliendo de la lista
    
    return match

if __name__ == "__main__":

    tamano_de_lista = int(input("¿De qué tamaño desea la lista? : "))
    objetivo = int(input("¿Qué número desea encontrar?: "))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}  en la lista')
    print(f'Se realizaron {contador} iteraciones')
