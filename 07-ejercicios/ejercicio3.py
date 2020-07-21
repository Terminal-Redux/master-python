"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numero
naturales. Resolverlo con for y con while.

"""

# Bucle while
contador_while = 1
print("##### INICIA BUCLE WHILE #####")
while contador_while < 61:
    print(f"{contador_while * contador_while}")
    contador_while += 1
else:
    print("##### TERMINA BUCLE WHILE #####")

# Bucle for
print("\n##### INICIA BUCLE FOR #####")
for contador_for in range(1,61):
    print(f"{contador_for * contador_for}")
else:
    print("##### TERMINA BUCLE FOR #####")