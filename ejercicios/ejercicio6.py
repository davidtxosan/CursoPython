"""
Pedir al usuario 2 numeros y mostrar los numeros inpares que esten en ese rango de numeros.
"""
numero1 = int(input("introduce el primer número: "))
numero2 = int(input("introduce el segundo número: "))

if numero2<numero1:
    print("el segundo numero debe ser mayor que el primero")
else:
    
    if numero1%2==0:
        for i in range((numero1+1),(numero2+1),2):
             print(i)
    else:
        for i in range(numero1,(numero2+1),2):
            print(i)
        