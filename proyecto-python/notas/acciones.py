from nota import Nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f "OK {usuario[1]}!! Vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de tu nota")
        descripcion = input("Introduce una descripción para tu nota ")

        nota = modelo(usuario[0],titulo, descripcion)
        
        guardar = nota.guardar()

        if guardar[0] >=1:

            print(f"Perfecto has guardado la nota llamada {nota.titulo}")
        else:
            print(f"\n no se ha guardado la nota, lo siento {}")
        

        

        

     
        

    