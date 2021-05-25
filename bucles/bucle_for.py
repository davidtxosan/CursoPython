numero_usuario = int(input("Elija un numero para multiplicar: "))
if numero_usuario <1:
    numero_usuario=1
for numero_tabla in range(1, 11):
    print(f"{numero_tabla} x {numero_usuario} = {numero_usuario*numero_tabla}")