"""
añadir valores a una lista mientras los valores sean menor de 120 y luego mostrar la lista
"""
lista = []

"""
con intervención del usuario:
numero=0
while numero <120:
    numero = int(input("introduce un numero hasta 120: "))
    if numero<120:
        lista.append(numero)
    else:
        print("Hasta aqui hemos llegado. ")
print(lista)
"""
# de forma automatica
for contador in range(0,120):
    lista.append(f"elemento:{contador}")
    print("mostrando el " + lista[contador])
print(lista)

print("\n#### con uso de bucle While ###")
contador =0
while contador < 120:
    lista.append(f"elemento:{contador}")
    print("mostrando el " + lista[contador])
    contador+=1
print(lista)

