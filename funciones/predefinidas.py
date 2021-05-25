nombre = "David Sanchez"

#funciones predefinidas
print(type(nombre))
#detectar el tipado
comprobar = isinstance(nombre,str)
if comprobar:
    print("esa variable es un string")
else:
    print("esa variable NO es un string")

if not isinstance(nombre, float):
    print("la vaiable no es un numero con decimales.")
#limpiar espacios

frase = "  contenido  con  espacios"
print(frase)
print(frase.strip())
#eliminar variables
year=2020
print(year)
del year
#comprobar variables vacias
texto= " ff "
if len(texto) <0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido:",len(texto))
#encontrar caracteres
frase= "la vida es bella"
print(frase)
print(frase.find("vida"))

#reemplazar palabras o caracteres en un string

nueva_frase= frase.replace("vida","moto")
print(nueva_frase)
#mayusculas y minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())