from notas import nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"OK {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota :")
        descripcion = input("Introduce una descripción para tu nota :")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:

            print(f"Perfecto has guardado la nota llamada :{nota.titulo}")
        else:
            print(f"\n no se ha guardado la nota, lo siento. {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nVale, {usuario[1]}, aquí tienes tus notas")
        nota = modelo.Nota(usuario[0])
        listado = nota.listar()

        for nota in listado:
            print("*************")
            print(f" titulo: {nota[2]}")
            print("-------------")
            print(f" Contenido: {nota[3]}")
            print("*************")

    def borrar(self, usuario):
        print(f"\n De acuerdo {usuario[1]}, vamos a borrar la nota")
        titulo = input("Introduce el titulo de la nota a borrar :")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print("registro eliminado")
        else:
            print("no se ha podido eliminar el registro")
