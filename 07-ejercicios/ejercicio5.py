"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario

"""
numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))

if numero1 < numero2:
    for contador in range(numero1 + 1, numero2):
        print(str(contador))

else: 
    print("El número 1 debe ser menor al numero 2")