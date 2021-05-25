# como usar cona funciones con dos funciones como parametros
print("\n######## EJEMPLO 1 ####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):

    texto = f"Los apellidos son: {apellidos}"
    return texto
def devuelvetodo(nombre,apellidos):
    texto = getNombre(nombre)+ "\n" + getApellidos(apellidos) 
    return texto

print(devuelvetodo("david", "Sanchez Jaramillo"))

