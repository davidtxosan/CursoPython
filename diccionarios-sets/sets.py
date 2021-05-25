"""
SET es un tipo de datos para tener una coleccion de valores,pero no tiene ni indice ni orden.
"""
#si se ponen elementos repetidos,solo imprime uno:
personas = {"Victor","Manolo","Victor"}
print(personas)

#tampoco respeta el orden de los elementos a la hora de imprimir
personas = {"David","Manolo","Victor"}
print(personas)

#el tipo de elemento es de tipo "set"
print(type(personas))

#agregar un elemento:
personas.add("juanito")
print(personas)

#eliminar un elemento(discard,remove,pop y clear):
personas.remove("Victor")
print(personas)

#como no tienen indices la unica forma de recorrer los elementos es con un bucle for(ordena ademas los elementos):

for elementos in personas:
    print(elementos)

#se suele usar los sets para saber si hay elementos duplicados en una colección,lista,etc y eliminarlos.

lista=[1,2,4,5,2,3,1,5,3,8,10,1,2]
print(lista)
lista_convertida= set(lista)
print(lista_convertida)



#Tambien para utilizarlos en operaciones de Algebra de conjuntos:Unión(|),intersección(&),diferencia(-),diferencia simétrica(^),inclusión(<=),conjuntos
#disyuntos(isdisjoint()),igualdad de conjuntos(==)
print("\n##### metodos conjuntos ###")
set1={1,2,3,4,5}
set2={1,2,5,6,7,8}
set3={1,2,3}
set4={1,2,3}
union= set1 | set2
intersec = set1 & set2
diferencia = set1 - set2
difSimetrica = set1 ^ set2
inclusion = set1 <= set2
inclusion2 = set3 <= set1
disyunto = set1.isdisjoint(set2)
igualdad = set1 == set2
igualdad2 = set3 == set4

print(union)
print(intersec)
print(diferencia)
print(difSimetrica)
print(inclusion)
print(inclusion2)
print(disyunto)
print(igualdad)
print(igualdad2)