contador = 1
while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador+=1

print("#######################")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador+=1
    
print(muestrame)