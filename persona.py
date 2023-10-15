class Persona:
    def __init__(self, nombre, edad,altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo=sexo
        
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, nueva_edad):
        self._edad = nueva_edad

    def getAltura(self):
        return self._altura

    def setAltura(self, nueva_altura):
        self._altura = nueva_altura

    def getSexo(self):
        return self._sexo

    def setSexo(self, nuevo_sexo):
        self._sexo = nuevo_sexo
        
    