#Ejemplo 1.parametros opcionales en funciones.Se pone un valor por defecto al parametro que queramos que sea opcional.

print("######## EJEMPLO 1 ####")

def getEmpleado(nombre, dni= None):

    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni!=None:
        print(f"dni: {dni}")
getEmpleado("david sanchez")

#Ejemplo2: return o devolución de datos

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    
    return saludo

print(saludame("david"))

#ejemplo 3 
print("\n######## EJEMPLO 2 ####")

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
def calculadora(numero1, numero2, basicas = False):

    suma= numero1 + numero2
    resta = numero1 - numero2
    multi = numero1*numero2
    division = numero1/numero2

    cadena = ""
    if basicas !=False:
        cadena+= "suma: " + str(suma)
        cadena += "\n"
        cadena+= "resta: " + str(resta)
        cadena += "\n"
    else:

        cadena+= "suma: " + str(suma)
        cadena += "\n"
        cadena+= "resta: " + str(resta)
        cadena += "\n"
        cadena+= "multiplicación: " + str(multi)
        cadena += "\n"
        cadena+= "division: " + str(division)
        cadena += "\n"

    return cadena
print(calculadora(numero1, numero2,True))






