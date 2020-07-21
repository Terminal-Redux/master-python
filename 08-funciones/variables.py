"""
Variables locales: Se definen dentro de la funcion y no
se puede usar fuera de ella, solo están disponibles dentro.

Variables globales: Son las que se declaran fuera de una funcion
y están disponibles dentro y fuera de ellas

"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres."

print(frase)

def holaMundo():
    frase = "Hola mundo!"
    print("Dentro de la funcion:")
    print(frase)

    year = 2021
    print(year)
    global website
    website = "capsus.mx"
    print("DENTRO: ", website)

    return "Dato devuelto " + str(year)

holaMundo();
print("FUERA: ", website)