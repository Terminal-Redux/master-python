"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido

"""

alumnos = 0
aprobados = 0
suspendidos = 0
while alumnos < 15:
    calificacion = int(input("Ingresa la calificacion: "))
    if calificacion < 0:
        calificacion =  0
    elif calificacion > 10:
        calificacion = 10
    if calificacion >= 6:
        aprobados += 1
    else:
        suspendidos +=1
    alumnos += 1
else:
    print(f"Alumnos aprobados: {aprobados} - Alumnos suspendidos: {suspendidos}")