"""
Proyexto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlras

"""
from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones()

accion = input("¿Qué quieres hacer? ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()