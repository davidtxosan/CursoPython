"""
pedir al usuario un número y después el porcentaje a sacar de ese numero.
"""

numero = int(input("introduce un número: "))
porcentaje = int(input("introduce el porcentaje a calcular del numero anterior solamente con numero sin %: "))

resultado=numero*(porcentaje/100)

print(f"El {porcentaje}% de {numero} es : {round(resultado,2)}") 