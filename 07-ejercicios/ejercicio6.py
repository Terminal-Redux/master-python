"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.

"""
for c1 in range(1, 11):
    print(f"##### TABLA DEL {c1} #####")
    for c2 in range(1, 11):
        resultado = c1 * c2
        print(f"{c1} * {c2} = {resultado}")
    else:
        print("\n")