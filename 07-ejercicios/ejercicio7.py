""" 
Ejercicio 7. Hacer un programa que muestre todos los numeros impares
entre dos numeros que elija el usuario

"""
numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))

if numero1 < numero2:
    for contador in range(numero1 + 1, numero2):
        if contador % 2 != 0:
            print(contador)
else:
    print("El primer numero debe ser menor que el segundo numero")