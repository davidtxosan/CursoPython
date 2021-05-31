#Programacion orientada a objetos

# definición de una clase(molde para crear mas objetos de ese tipo)

class Coche:

    # atributos o propiedades de la clase
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # metodos de la clase(funcionen)

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

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

# fin de la definicion de la clase

# crear objetos /Instanciar la clase

coche = Coche()
coche.setColor("verde")
coche.setModelo("Avensis")
print("el color del coche es: ", coche.getColor(), "la marca ", coche.getMarca(), "y el modelo es:", coche.getModelo(),"\n")
print("la velocidad del coche es " + str(coche.getVelocidad()) + "km/h")
coche.acelerar()
print("la velocidad del coche es " + str(coche.getVelocidad()) + "km/h")
coche.frenar()
print("la velocidad del coche es " + str(coche.velocidad) + "km/h")

print("----------------------------------------")
#creación de mas objetos
coche2 = Coche()
coche2.setColor("turquesa"), coche2.setModelo("Avendador")
print("el color del coche es: ", coche2.getColor(), "la marca ", coche2.getMarca(), "y el modelo es:", coche2.getModelo())