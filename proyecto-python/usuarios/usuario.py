import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


# creamos la clase usuario con el metodo contructor y dos funciones
class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    """ en la función registrar creamos una variable "sql" con la sentencia para introducir valores en la tabla al
     registrar un usuario y "usuario" con los valores que se introduzcan por teclado.
    """

    def registrar(self):
        fecha = datetime.datetime.now()
        """
        utilizamos el modulo hashlib para cifrar la contraseña que introduce el usuario.Necesita que el dato que
        hay que cifrar esté en byte,por eso se usa .enconde para cambiar el tipo.
        """
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s,%s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        # tratamos las excepciones en caso de registro erróneo
        try:

            # ejecutamos la consulta  con las dos variables anteriores
            cursor.execute(sql, usuario)

            # confirmamos los cambios
            database.commit()

            # nos devuelve la cantidad de registros creados
            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        return result

    def identificar(self):

        # consulta para saber si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # cifrar
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
