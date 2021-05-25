cantantes= ["queen","Iron Maiden","Dire Straits","Extremoduro","Platero y tú"]
peliculas=["batman","spiderman","el señor de los anillos"]
numeros =[1, 2 ,5, 8, 3, 4]
#ordenar los elementos de una lista
numeros.sort()
print(numeros)
#modificación de los indices:
peliculas[1]="Gran Torino"

print(cantantes)
#agregar 1 elemento a una lista:
cantantes.append("Michael Jackson")
print(cantantes)
#agregar un elemento en una posicion especifica:
cantantes.insert(1,"Bisbal")
#eliminar el ultimo elemento:
cantantes.pop()
#eliminar un elemento por posicion de su indice:
cantantes.pop(1)
#eliminar un elemento(cualquiera)
cantantes.remove("queen")
print(cantantes)

#para añadir varios elementos a una lista existente,creamos una nueva lista con los elementos y los unimos a la primera lista con "extend":
cantantes2=("Kiss","Fito")
cantantes.extend(cantantes2)
print(cantantes)

#dar la vuelta a la lista:
cantantes.reverse()
print(cantantes)
#buscar si existe un elemento dentro de la lista(devuelve True o False)
print("Kiss" in cantantes)
# contar elementos
print(len(cantantes))
#cuantas veces aparece un elemento de la lista
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))
#averiguar el indice de un elemento
print(cantantes.index("Fito"))
#averiguar el elemento por la posicion de su indice
print(cantantes[2])
