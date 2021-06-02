from usuarios import usuario as modelo
from ..notas import acciones 

class Acciones:

    def Registro(self):

        print("\nOk! Vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre? : ")
        Apellidos = input("¿Y tus Apellidos? : ")
        email = input("Introduce tu email : ")
        passwd = input("Introduce tu contraseña: ")

        usuario = modelo.Cliente(nombre, Apellidos, email, passwd)
        registro = Cliente.registrar()
                
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}" )
        else:
            print("\nno te has registrado correctamente")
        

    def Login(self):

        print("\nintroduce tu mail y contraseña")

        try:
            email =  input("Introduce tu email : ")
            passwd = input("Introduce tu contraseña: ")

            usuario = modelo.Cliente('', '', email, passwd)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido  {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto.Intentalo de nuevo.")

    def proximasAcciones(self, usuario):


        print("""
        
        Acciones disponibles:
        -Crear nota(crear)
        -Mostrar tus notas(mostrar)
        -Eliminar nota(eliminar)
        -salir (salir)

        """)

        accion = input("¿Qué quieres hacer?")
        hazEl = acciones.Acciones()

        if accion == "crear":
            print("vamos a crear una nota")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        if accion == "mostrar":
            print("vamos a mostrar una nota")
            self.proximasAcciones(usuario)

        if accion == "eliminar":
            print("vamos a eliminar una nota")
            self.proximasAcciones(usuario)
            
        if accion == "salir":
            print(f"\nHasta pronto {usuario[1]}")
            exit()




