print (" ############# TABLAS DE MULTIPLICAR ###########")

for cabecera in range(1,11):
    print("######################")
    print(f"### Tabla del {cabecera} ####")
    print("######################")

    print("\n")
    for numero in range(1,11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")
    
    print("\n")