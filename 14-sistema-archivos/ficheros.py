from io import open
import pathlib, shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir
archivo.write("*******Soy un texto metido desde python********\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    # lista_frase = frase.split()
    # print(lista_frase)
    print("- " + frase.center(100))

# Copiar
"""ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado88.txt"

shutil.copyfile(ruta_original, ruta_alternativa)"""

# Mover
"""ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"

shutil.move(ruta_original, ruta_nueva)"""

# Eliminar
import os
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"
os.remove(ruta_nueva)"""

# Comprobar si existe
import os.path

if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")
# print(os.path.abspath("../"))