"""
Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un string,
un etnero y un booleano y que imprima un mensaje
segun el tipo de dato de cada variable

"""

def traducirTipo(tipo):
    result = ""
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    
    return result

def revisarTipoVariable(data, tipo):
    test = isinstance(data, tipo)
    resultado = ""
    if test:
        resultado = f"Tipo de variable de {data}: {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return resultado

lista = ["hola", 13, 94, "adios"]
cadena = "Hola mundo"
entero = 45
booleano = True

print(revisarTipoVariable(lista, type(lista)))
print(revisarTipoVariable(cadena, type(cadena)))
print(revisarTipoVariable(entero, type(entero)))
print(revisarTipoVariable(booleano, type(booleano)))