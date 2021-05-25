"""
crear una lista con 8 numeros enteros.
-recorrerla e imprimirla
-ordenarla e imprimirla
-mostrar su longitud
-buscar un elemento dentro de la lista en base a lo que el usuario nos pida por teclado

"""
print("parte 1:creación de la lista ")
numeros = [18,3,51,69,21,37,84,13,92]
print("Recorriendo la lista sin funciones: ")

for numero in numeros:
    print(numero)
print("Recorriendo la lista CON una función: ")

def recorrer(lista):

    for numero in lista:
        print(str(numero))
         
recorrer(numeros)
print("\n")
recorrer(["david","juan","victor"])

print("\nparte 2: ordenación de la lista ") 

numeros.sort()
print(numeros)

print("\nparte 3 Mostrar longitud de la lista ")

print(f"la longitud de la lista es de {len(numeros)} numeros")

print("\nparte 4 busqueda de un caracter dentro de la lista")


num= int(input("¿que número deseas buscar en la lista?: "))

comprobar = isinstance(num, int)

print(comprobar)
while not comprobar:
    num= int(input("¿que número deseas buscar en la lista?: "))
if num in numeros:
    print(f"el numero {num} esta en la lista")
else:
    print(f"El numero {num} NO está en la lista")

