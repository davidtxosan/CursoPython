import mysql.connector
def conectar():
    #creamos una variable con los datos de conexion a la base de datos
    database = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd ="",
    database = "master_python",
    port= 3306
    )

    #creamos el cursor para poder hacer consultas sql
    cursor = database.cursor(buffered=True)
    #nos retorna un lista con la conexio en la posicion 0 y el cursor en la posicion 1
    return [database, cursor]