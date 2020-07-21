"""
Ejercicio 8.  ¿Cuanto es el X por ciento de Y numero?
                            20% de 150
"""

numero = int(input("Escribe un numero: "))
porcentaje = int(input(f"¿Que porcentaje quieres obtener de {numero}? "))

resultado = numero * (porcentaje / 100)
print(f"El {porcentaje}% de {numero} es: {resultado}")