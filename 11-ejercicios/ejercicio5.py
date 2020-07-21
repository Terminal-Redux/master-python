""" 
Ejercicio 5.
Crear una lista con el contenido de esta tabla:

ACCION  AVENTURA    DEPORTES
GTA     ASSINS      FIFA 21
COD     CRASH       PRO 21
PUBG    PoP         MOTO GP 21

Mostrar esta informacion ordenada
"""
def get_categoria(cat):
    return cat.get('genero')

tabla = [
    {
        "nombre": "GTA",
        "genero": "ACCION"
    },
    {
        "nombre": "COD",
        "genero": "ACCION"
    },
    {
        "nombre": "PUBG",
        "genero": "ACCION"
    },
    {
        "nombre": "ASSINS",
        "genero": "AVENTURA"
    },
    {
        "nombre": "CRASH",
        "genero": "AVENTURA"
    },
    {
        "nombre": "PoP",
        "genero": "AVENTURA"
    },{
        "nombre": "FIFA 21",
        "genero": "DEPORTES"
    },
    {
        "nombre": "PRO 21",
        "genero": "DEPORTES"
    },
    {
        "nombre": "MOTO GP 21",
        "genero": "DEPORTES"
    }
]

tabla.sort(key=get_categoria)

for registro in tabla:
    print(f"Categoría: {registro['genero']} - Nombre: {registro['nombre']}")