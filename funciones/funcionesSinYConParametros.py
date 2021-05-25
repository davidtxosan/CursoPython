# ejemplo 1 de funcion
"""
print("######## EJEMPLO 1 #####")

def muestraNombres():
    print("Victor")
    print("David")
    print("Aitor")
    print("Nestor")
    print("Juan")
    print("Paco")

muestraNombres()
"""
# EJEMPLO 2 .FUNCIONES CON PARAMETROS
"""
print("######## EJEMPLO 2 #####")

nombre = input("introduce tu nombre: ")
edad = int(input("introduce tu edad: "))

def mostrarTuNombre(nombre, edad):

    print(f"Tu nombre es: {nombre}")
    if edad>=18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")

mostrarTuNombre(nombre,edad)

"""
print("######## EJEMPLO 3 ####")

numero = int(input("Introduce el numero de la tabla de multiplicar: "))
def tabla(numero):
    
    print(f"Tabla de multiplicar del numero: {numero}")
    print("")
    

    for contador in range(1,11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")
tabla(numero)

# Ejemplo 3.1 sacar todas las tablas de multiplicar metiendo la función dentro de un bucle

print("-------------------------------------------")
for numeroTabla in range(1,11):
    tabla(numeroTabla)

