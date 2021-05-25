def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

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