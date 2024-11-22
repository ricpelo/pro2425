"""
12. Escribir un programa que gestione datos almacenados en una lista, de
forma que muestre un menú con las siguientes opciones:
1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
El programa deberá pedir la información necesaria para cada opción elegida
por el usuario.
"""

def mostrar_menu():
    """Muestra el menú"""
    print("""
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.""")


def elegir_opcion():
    """Pide al usuario la opción que desea."""
    return input("Introduzca la opción deseada: ")


def anyadir_elemento(lst):
    """Añade un elemento a la lista."""
    elem = input("Introduzca el elemento a añadir: ")
    lst.append(elem)
    print("Ahora la lista contiene el elemento", elem)


def mostrar_elementos(lst):
    """Muestra los elementos de la lista."""
    # print("[" + ", ".join(lst) + "]")
    print(lst)


def cambiar_elemento(lst):
    """Cambia un elemento de la lista por otro."""
    if lst == []:
        print("La lista está vacía.")
        return
    mostrar_elementos(lst)
    indice = int(input("Introduzca el índice del elemento a cambiar: "))
    elem = input("Introduzca el elemento nuevo: ")
    lst[indice] = elem


def eliminar_elemento(lst):
    """Elimina un elemento de la lista."""
    if lst == []:
        print("La lista está vacía.")
        return
    indice = int(input("Introduzca el índice del elemento a eliminar: "))
    del lst[indice]


lista = []
while True:
    try:
        mostrar_menu()
        opc = elegir_opcion()
        if opc == "1":
            anyadir_elemento(lista)
        elif opc == "2":
            cambiar_elemento(lista)
        elif opc == "3":
            eliminar_elemento(lista)
    #    elif opc == "4":
    #        eliminar_todos(lista)
        elif opc == "5":
            mostrar_elementos(lista)
        elif opc == "0":
            break
        else:
            print("Opción incorrecta")
    except ValueError:
        print("El índice introducido no es un número")
    except IndexError:
        print("El índice introducido no es válido.")   

