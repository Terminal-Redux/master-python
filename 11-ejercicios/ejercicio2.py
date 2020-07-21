""" 
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar while y for

"""
coleccion = []

for contador in range(0, 120):
    coleccion.append(contador)
print(coleccion)

contador = 0
while len(coleccion) < 120:
    coleccion.append(contador)
    contador += 1
print(coleccion)

