"""
crear 4 variables:
1.tipo lista
2.tipo entero
3.tipo string
4.tipo booleano

el programa va a imprimir que tipo de variable es cada una.
hacer con y sin funciones
"""
lista=["david", "Juan", "María", "Juana"]
entero= 345
nombre="Maria de las Mercedes"
Mujer=False

print("\n ####### tipos de variables#######3")
print(f"\nEl tipo {lista} es: {type(lista)}")
print(f"\nEl tipo {entero} es: {type(entero)}")
print(f"\nEl tipo {nombre} es: {type(nombre)}")
print(f"\nEl tipo {Mujer} es: {type(Mujer)}")

print("\nUso de funciones")
def comprobaciones(tipo):
    return f"la variable {tipo} es :{type(tipo)}"

print(comprobaciones("Hola"))
print(comprobaciones(365))
print(comprobaciones(True))