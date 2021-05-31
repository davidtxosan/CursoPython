import os
import shutil
#crear una carpeta
"""
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
    print("el directorio  ya existe.Borrando directorio y creando uno nuevo")
    os.rmdir("./mi carpeta")
    os.mkdir("./mi carpeta")
"""
#otra forma de hacerlo con el parametro exist_ok= True
#os.makedirs("./mi carpeta", exist_ok=True)

#eliminar una carpeta
#os.rmdir("./mi carpeta")
"""
#para copiar una carpeta hay que importar la libreria shutil y el comando copytree,con el comando copyfile da error.
ruta_antigua= "./mi carpeta"
ruta_nueva = "./mi carpeta_nueva"
shutil.copytree(ruta_antigua, ruta_nueva)
"""
#listar contenido de una carpeta
contenido = os.listdir("./mi carpeta")
for fichero in contenido:
    print("fichero: " + fichero)