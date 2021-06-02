import mysql.connector


def conectar():
    # creamos una variable con los datos de conexión a la base de datos
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306
    )

    # creamos el cursor para poder hacer consultas sql
    cursor = database.cursor()
    # nos retorna un lista con la conexión en la posición 0 y el cursor en la posición 1
    return [database, cursor]
