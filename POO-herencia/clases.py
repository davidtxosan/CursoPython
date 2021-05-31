class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.Altura

    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "estoy hablando"
    
    def caminar(self):
        return "estoy caminando"

    def dormir (self):
        return "estoy durmiendo"

class Informatico(Persona):
    """
    lenguajes = "HTML Y CSS"
    experiencia = 5

    """

    def __init__(self):

        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "estoy programando"

    def repararPc(self):
        return "estaré reparando tu ordenador"

class TecnicoRedes(Informatico):

    def __init__(self):
        # invocamos al contructor de la clase padre para obtener sus valores y poder utilizarlos luego
        super().__init__()
        self.auditarRedes = "experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "estoy auditando una red"

