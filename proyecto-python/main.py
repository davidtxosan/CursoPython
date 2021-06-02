import pathlib

# la librería getpass permite que no se vea los caracteres al introducir la contraseña
# import getpass
# importo la función Acciones del modulo acciones y le pongo un alias para que sea mas comprensible
from usuarios import acciones

HazEl = acciones.Acciones()
"""
Proyecto Python y Mysql:
-Abrir asistente
-login o registro
-Si elegimos registro, creará un usuario en la BBDD
-Si elegimos login,identificará al usuario y nos preguntará
-Crear nota, mostrarla o borrarlas
"""

print("""
Acciones disponibles:
    - registro
    - Login

""")

accion = input("¿Qué quieres hacer?\n")
if accion == "registro":
    HazEl.registro()

elif accion == "login":
    HazEl.login()
