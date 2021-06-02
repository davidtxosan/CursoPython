import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):

        print("\nOk! Vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre? : ")
        apellidos = input("¿Y tus Apellidos? : ")
        email = input("Introduce tu email : ")
        passwd = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, passwd)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nno te has registrado correctamente")

    def login(self):

        print("\nintroduce tu mail y contraseña")

        try:
            email = input("Introduce tu email : ")
            passwd = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, passwd)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido  {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximas_acciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto.Intentalo de nuevo.")

    def proximas_acciones(self, usuario):

        print("""
        
        Acciones disponibles:
        -Crear nota(crear)
        -Mostrar tus notas(mostrar)
        -Eliminar nota(eliminar)
        -salir (salir)

        """)

        accion = input("¿Qué quieres hacer?")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximas_acciones(usuario)

        if accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximas_acciones(usuario)

        if accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximas_acciones(usuario)

        if accion == "salir":
            print(f"\nHasta pronto {usuario[1]}")
            exit()
