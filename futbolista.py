
from persona import Persona
from deportista import Deportista


class Futbolista(Deportista, Persona):
    listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, sexo,  años,golesMarcados, tarjetasRojas,piernaHabil):
        Persona.__init__(self, nombre,edad,altura,sexo)
        Deportista.__init__(self, años)
        
        
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)
        
    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, nuevosGoles):
        self._golesMarcados = nuevosGoles

    # Getter y Setter para tarjetasRojas
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, nuevasTarjetas):
        self._tarjetasRojas = nuevasTarjetas

    # Getter y Setter para piernaHabil
    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, nuevaPierna):
        self._piernaHabil = nuevaPierna
    @classmethod
    def getListaFutbolistas(self):
        return Futbolista._listaFutbolistas

    @classmethod
    def setListaFutbolistas(self, lista):
        Futbolista._listaFutbolistas = lista

        
        
    def __str__(self):
        return f"Mi nombre es {self.getNombre()}, soy profesional en el deporte {self.getDeporte()}, tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte."