import sqlite3

#conexion a sqlite y creación de una base de datos

conexion = sqlite3.connect("pruebas.db")

# crear cursor para ejecutar las consultas 

cursor = conexion.cursor()
# crear tabla y ponemos triple comillas para crear una consulta multilinea

cursor.execute("""

CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT , 
    titulo VARCHAR(255), 
    descripcion text ,
    precio int (255)
);

""")
# confirmar los cambios

conexion.commit()

#insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'descripcion del producto', 550)")
conexion.commit()
"""

#borrar registros

cursor.execute("DELETE FROM productos")



# listar los datos por pantalla

cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(productos)

#recorrer los datos con un bucle for

for producto in productos:
    print (producto)

# o que me imprima por pantalla solo uno de los campos

for producto in productos:
    print("----------")
    print("id: ",producto[0])
    print("nombre: ", producto[1])
    print("descripción: ",producto[2])
    print("precio: ", producto[3])

#cerrar conexion para que se guarden los datos
conexion.close()
