print("\n ************* lista de contactos *************")
contactos = [
    ["Antonio","lopez","antonio@antonio.com"],["Salvador","santamaria","Salvador@salvador.com"],["luis","perez","luis@luis.com"]
]
print(contactos)
print("\n")
print(contactos[2])
print("\n")
print(contactos[2][1])
print("\n")
#recorrer todos los contactos de la lista(3 sublistas)
for contacto in contactos:
    print(contacto)
print("\n")
#recorrer solo una de las sublistas
for contacto in contactos[2]:
    print (contacto)
print("\n")
#recorrer solo el nombre de las 3 listas
for contacto in contactos:
    print(contacto[0])
print("\n")
#o el nombre y el email de las 3 listas
for contacto in contactos:
    print(contacto[0])
    print(contacto[2])
    print("\n")
#recorrer cada elemento de una sublista con un bucle for dentro de otro y con condicionales:

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            print(f"Nombre: {elemento}")
        elif contacto.index(elemento)==1:
            print(f"Apellidos: {elemento}")
        else:
            print(f"Email: {elemento}")
            
    print("\n")