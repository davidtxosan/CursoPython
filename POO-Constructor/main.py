from coche import Coche
carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro2 = Coche("verde", "seat", "panda", 150, 150, 4)
carro3 = Coche("rojo", "citroen", "xara", 150, 100, 5)
carro4= Coche("azul", "mercedez", "benz", 150, 140, 5)

print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

#detectar tipado
carro3 = "aleatorio"
if type(carro3) == Coche:
    print("es un objeto correcto!!)")
else:
    print("no es un objeto")

#visibilidad de los objetos

print(carro.soy_publico)
print(carro.getPrivado())