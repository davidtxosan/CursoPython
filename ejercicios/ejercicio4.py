"""
Ejercicio que pide 2 numeros al usuario y genera los numeros comprendidos entre ellos.
"""
numero1 = int(input("introduce el primer numero: "))
numero2 = int(input("introduce el segundo numero: "))

if numero2<numero1:
    print(f"el {numero1} es menor que {numero2} y no se puede hacer un rango positivo entre ambos.")
else:
    print(f"los numeros entre {numero1} y {numero2} son :")

    for i in range((numero1+1),numero2):
     print (i)