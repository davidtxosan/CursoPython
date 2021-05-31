class Coche:

    # atributos o propiedades de la clase
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    soy_publico = "hola, soy un atributo público"
    __soy_privado = "hola, soy un atributo privado"

    # metodo constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    # metodos de la clase(funciones)

    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getCaballaje(self):
        return self.caballaje
        
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        
        return self.velocidad

    def getPlazas(self):
        return self.plazas

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getInfo(self):
        
        info = "------información del coche----"
        info += "\n color :" + self.getColor()
        info += "\n Marca :" + self.getMarca()
        info += "\n Modelo :" + self.getModelo()
        info += "\n velocidad máxima :" + str(self.getVelocidad())
        info += "\n caballaje :" + str(self.getCaballaje())
        info += "\n plazas :" + str(self.getPlazas())

        return info
