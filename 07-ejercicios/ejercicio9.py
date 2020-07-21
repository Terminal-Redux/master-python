"""
Ejercicio 9. Hacer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111

"""
contador = 1
while contador < 100:
    numero = int(input("Escribe un numero: "))
    if numero == 111:
        print("Felidades, adivinaste el numero.")
        break
    else:
        print(f"El numero {numero} no es el que busco. Vuelve a intentarlo.\n")
else:
    print("Felicidades, adivinaste el numero.")