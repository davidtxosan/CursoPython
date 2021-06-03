from tkinter import *


# vamos a crear la clase programa con todo el codigo dentro

class Programa:

    def __init__(self):
        self.title = "Master en Python con Udemy"
        self.icon = './imagenes/favicon.ico'
        self.icon_alt = './imagenes/favicon-16x16.ico'
        self.size = "600x480"
        self.resizable = False

    def cargar(self):
        # crear una ventana y ponerle un tamaño

        ventana = Tk()
        ventana.geometry(self.size)

        # bloquear el redimensionamiento(alto y ancho)
        if self.resizable :
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)


        # ponerle un logotipo a la ventana o favicon
        ventana.iconbitmap(self.icon)

        # poner titulo a la ventana

        ventana.title(self.title)

        # arrancar y mostrar la ventana.Debe estar al final del script.
        ventana.mainloop()
# Instanciar mi objeto

programa = Programa()
programa.cargar()