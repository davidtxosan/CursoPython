"""
Es un tipo de dato que almacena un conjunto de datos en formato clave : valor.
Se parece a un objeto JSON o array asociativo
"""

persona = {

    "nombre":"David",
    "Apellidos":"Sanchez Jaramillo",
    "web":"davidweb.es"
}

#print(persona)
#print(persona["nombre"])

# lista con diccionarios

contactos = [
    {
        "nombre":"Antonio",
        "email":"antonio@antonio.com"
    },
    {
        "nombre":"Luis",
        "email":"luis@luis.com"
    },
    {
        "nombre":"Salvador",
        "email":"salvador@salvador.com"
    }

]

print(contactos)
#imprime solo el diccionario que esta en la posicion 0 dentro de la lista
print(contactos[0])
#cambia el valor que esta en el diccionario en la posicion 0 de la lista y con el campo "nombre".
contactos[0]["nombre"]="Antoñito"
print(contactos[0]["nombre"])
print("\n")

#bucle para recorrer todos los diccionario de la lista e imprimirlos
for contacto in contactos:
    print(contacto)
#bucle para recorrer todos los diccionarios,pero solo imprimir el valor del campo "nombre" de los diccionarios.
print("\nLISTADO DE CONTACTOS :")
print("-----------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto :{contacto['nombre']}")
    print(f"Email del contacto :{contacto['email']}")
    print("-----------------------------------")