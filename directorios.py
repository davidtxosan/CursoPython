import os
"""
#crear una carpeta
if not os.path.isdir("·/mi carpeta"):
    os.mkdir("./mi carpeta")
else:
    print("el directorio  ya existe")
"""
#haciendolo asi me da una excepción si el directorio ya existe,esta es la forma correcta para que funcione
"""
try:

    os.mkdir("./mi carpeta")
except OSError:
    if not os.path.isdir("./mi carpeta"):
       raise
    print("el directorio  ya existe")
"""
#otra forma de hacerlo con el parametro exist_ok= True
os.makedirs("./mi carpeta", exist_ok=True)