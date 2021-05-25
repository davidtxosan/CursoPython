"""
pedir al usuario un numero y hasta que no introduzcamos 111 nos seguira pidiendo el número indefinidamente.
"""

numero = int(input("introduzca un número: "))

while numero != 111:

    print(f"ha introducido el número {numero}")
    numero = int(input("vuelva a introducir el número: "))
else:

    print("Felicidades, ha introducido el número correcto")