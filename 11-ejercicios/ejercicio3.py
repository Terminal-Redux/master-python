""" 
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minúsculas y mostrarlo
en mayusculas.

"""
texto = " "
if len(texto.strip()) <= 0:
    print("La cadena está vacia. Rellenandola: ")
    texto = "hola mundo estoy en minusculas"
    print(texto.upper())
else:
    print("La cadena ya tiene contenido: " + texto)