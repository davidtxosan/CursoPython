"""
crear un programa que compruebe si una variable esta vacia.SI es asi,rellenarla con texto en minuscula y mostrarlo en mayuscula
"""
texto= " "
if len(texto.strip()) <=0:
    texto="soy un texto en minusculas "
    print(texto.upper())
else:
    print(texto)