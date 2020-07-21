"""
Modulos: Son funcionalidades ya hechas para reutilizar.
En python hay muchos modulos, que los puedes consulta aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.

"""
# Importar modulo propio
# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

# print(mimodulo.holaMundo("Amilcar Gonzalez"))
# print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Amilcar Gonzalez"))
print(calculadora(3, 5, True))

# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().time())

# Modulo matematicas
import math

print("Raíz cuadrada de 10: ", math.sqrt(10))

print("Numero Pi: ", float(math.pi))

print("Redondear: ", math.floor(6.56789))

print("Redondear: ", math.ceil(6.56789))

# Modulo random
import random

print("Número de la suerte entre 15 y 67: ", random.randint(15,67))