"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las
operaciones básicas de una calculadora y mostrarlo por pantalla.

"""
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))

print("\n##### SUMA #####")
resultado = numero1 + numero2
print(f"{numero1} + {numero2} = {resultado}")

print("\n##### RESTA #####")
resultado = numero1 - numero2
print(f"{numero1} - {numero2} = {resultado}")

print("\n##### MULTIPLICACION #####")
resultado = numero1 * numero2
print(f"{numero1} * {numero2} = {resultado}")

print("\n##### DIVISION #####")
resultado = numero1 / numero2
print(f"{numero1} / {numero2} = {resultado}")