class Persona:
    def __init__(self, nombre, edad,altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo=sexo
        
    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        self._edad = nueva_edad

    def get_altura(self):
        return self._altura

    def set_altura(self, nueva_altura):
        self._altura = nueva_altura

    def get_sexo(self):
        return self._sexo

    def set_sexo(self, nuevo_sexo):
        self._sexo = nuevo_sexo
        
    