import mysql.connector

# conexion(hay que crear la base de atos primero con cursor)
conexion = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "",
    database = "master_python"

)

cursor = conexion.cursor()
# creacion de la base de datos

"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment primary key ,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null

)

""")
"""
cursor.execute("show tables")

for table in cursor:
    print(table)
"""
# insertar registros en la tabla

# cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500)")

# insertar registros de manera masiva creando una lista
coches = [

    ('Seat', 'Ibiza', 5500),
    ('Renault', 'Clio', 9200),
    ('Toyota', 'Avensis', 8200),
    ('Citroen', 'Saxo', 7500)


]
# se pone %s por cada uno de los valores de la lista y como segundo parametro la lista en sí

# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)",coches)

#con el commit confirmamos el comando
conexion.commit()

# mostrar contenido de la tabla con filtros
cursor.execute("SELECT * FROM vehiculos WHERE precio <=9000")
result = cursor.fetchall()

print("----------- TODOS MIS COCHES -------------\n")
for coche in result:
    print(coche[0],coche [1], coche[2])

#borrar registros

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Toyota' ")

#si da error poner en el parametro de creación del cursor la opcion buffered = true
conexion.commit()

#para saber cuantos registros han sido modificados o borrados se puede hacer con la opcion cursor.rowcount + un mensaje
print("---------")
print(cursor.rowcount, " registros borrados")

#actualizar registros de la base de datos

cursor.execute("UPDATE vehiculos SET modelo= 'Leon' WHERE marca = 'Seat'")
print(cursor.rowcount, " registros modificados")
conexion.commit()