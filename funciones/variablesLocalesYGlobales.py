#variables globales
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres."
print(frase)

def holamundo():
    frase = "hola Mundo!"
    print("dentro de la función:")
    print(frase)

    year= 2021
    print(year)
    
    global website
    website = "victorroblesweb.es"
    print("dentro de la funcion: ",website)
    
    return "dato devuelto " + str(year)
    
print(holamundo())
print(f"fuera de la funcion: {website}")


