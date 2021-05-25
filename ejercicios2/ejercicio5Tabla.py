"""
crear una lista con el contenido de esta tabla:
accion          aventura                     deportes
GTA         ASSASINS CREED                  fifa 21
COD             CRASH                       pro 21
PUGB        Prince of persia                moto gp 21

mostrar la informacion ordenada

"""

tabla = [

    {
        "categoria": "ACCION",
        "juegos":["GTA","Call of duty", "PUGB"]

    },
    {   
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS CREED","CRASH","Prince of persia"]

    },
    {   "categoria": "DEPORTES",
        "juegos":["FIFA 21","PRO 21","MOTO GP 21"]

    }
]

for categoria in tabla:
    print(f"-------{categoria['categoria']}--------------")
    for juego in categoria['juegos']:
        print(juego)
