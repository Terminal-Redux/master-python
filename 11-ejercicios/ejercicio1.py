""" 
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 numeros enteros y haga lo siguiente:
-   Recorrer la lista y mostrarla
-   Hacer funcion que recorra listas de numeros y devuelva un string
-   Ordenarla y mostrarla
-   Mostrar su longitud
-   Buscar algun elemento que el usuario pida por teclado

"""
# Funcion que recorre lista y 
def mostrarLista(lista):
    cadena = ""
    for elemento in lista:
        cadena += str(elemento) + "\n"
    return cadena
# Crear lista
numeros = [4, 6, 1, 13, 8, 10, 5, 23]

# Recorrer y mostrar
print("Lista inicial")
print(mostrarLista(numeros))

numeros.sort()

print("\nLista ordenada")
print(mostrarLista(numeros))

# Mostrar longitud
try:
    print(f"Longitud de la lista: {len(numeros)}")

    # Busqueda en la lista
    numero_usuario = int(input("¿Qué numero deseas buscar? "))
    comprobar = isinstance(numero_usuario, int)
    while not comprobar or numero_usuario <= 0:
        numero_usuario = int(input("¿Qué numero deseas buscar? "))
    else:
        print(f"Has introducio el {numero_usuario}")

        search = numeros.index(numero_usuario)
        print(f"El número buscado existe en la lista, es el indice: {search}")

except:
    print("El número no está en la lista. Lo siento.")

"""

if numero_usuario in numeros:
    print(f"{numero_usuario} si está en la lista! :)")
else:
    print(f"{numero_usuario} no está en la lista :(")

"""