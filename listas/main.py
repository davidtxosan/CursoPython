pelicula= "batman"
peliculas=["batman","spiderman","el señor de los anillos"]
#segunda forma de crear una lista.Le pasamos una Tupla con la sentencia "list"
cantantes= list(("drake","2pac","queen"))
# o con un rango
years= list(range(2020,2050))
variada= ["david",2020,True,4.4]
"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
#uso de los indices:

print(peliculas[1])
print(peliculas[-1])
print(peliculas[1:])
print(cantantes[1:3])

#recorrer elementos de una lista 

print("\n--------------------------")

for pelicula in peliculas:
     print(f"{peliculas.index(pelicula)+1}.{pelicula}")
print("\n")
#añadir nuevas peliculas a peticion del usuario:
nueva_pelicula = ""
while nueva_pelicula !="parar":
    nueva_pelicula=input("introduce el titulo de la nueva pelicula:")
    if nueva_pelicula !="parar":
        peliculas.append(nueva_pelicula)
        
print("\n######### LISTADO DE PELICULAS ##########")
for pelicula in peliculas:
     print(f"{peliculas.index(pelicula)+1}.{pelicula}")     
