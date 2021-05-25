#depende desde donde se ejecute el comando(si desde VS o desde la consola del sistema),creará el archivo en uno u otro lugar.Si ponemos la opción "parent"
#crea el archivo dentro de la carpeta desde donde ejecutamos el archivo en VS.
from io import open
import pathlib
import shutil

#Abrir un archivo
ruta =str(pathlib.Path(__file__).parent) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

#Escribir en un archivo
archivo.write("soy un texto escrito de nuevo desde python\n")

#cerrar archivo
archivo.close()

#Abrir un archivo
ruta =str(pathlib.Path(__file__).parent) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r+")

#leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardarlo en una lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    lista_frase=frase.split()
    print(lista_frase)

#copiar un archivo
ruta_original =str(pathlib.Path(__file__).parent) + "/fichero_texto.txt"
ruta_destino =str(pathlib.Path(__file__).parent) + "/fichero_textCopia.txt"
ruta_alternativa ="./modulos/fichero_texto.txt"

shutil.copyfile(ruta_original, ruta_destino)