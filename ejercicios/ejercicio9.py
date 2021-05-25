"""
pedir al usuario la nota de 15 alumnos y el programa nos dirá cuantos alumnos han suspendido y cuantos han aprobado.
"""

aprobados= 0
suspensos = 0
contador = 1

numero_alumnos = int(input("¿cuantos alumnos tienes? "))

while contador <= numero_alumnos:

    nota = int(input(f"¿que nota quieres poner al alumno {contador} ? "))
    while nota > 10:
        nota = int(input("La nota debe estar entre 0 y 10.Vuelve a introducir la nota: "))

    if nota>=5:
        aprobados+=1
    else:
        suspensos+=1

    contador+=1
print(f"el numero de suspendidos es :{suspensos} y el de aprobados es : {aprobados}")   