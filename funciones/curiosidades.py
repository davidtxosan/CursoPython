# Es recomendable porner las funciones al inicio del codigo y juntas.
def mi_funcion():
    print("hola,que tal")
def mi_funcion2():
    print("hola,que tal2")

nombre= "david"
apellidos = "Sanchez"

print("hola mundo")
print(f"Bienvenido {nombre}")

mi_funcion
mi_funcion2

#tambien que las funciones devuelvan un dato,No que lo impriman(eso se hara cuando se invoque a la función)
def mi_funcion(nombre):
    return "hola,que tal"
def mi_funcion2(apellidos):
    return"hola,que tal2"

nombre= "david"
apellidos = "Sanchez"


print(mi_funcion(nombre))
print(mi_funcion2(apellidos))
