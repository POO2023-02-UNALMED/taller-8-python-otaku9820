
from persona import Persona
from deportista import Deportista


class Futbolista(Deportista, Persona):
    listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, sexo,  años,golesMarcados, tarjetasRojas,piernaHabil):
        Persona.__init__(nombre,edad,altura,sexo)
        Deportista.__init__( años)
        
        
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)
        
    def get_golesMarcados(self):
        return self._golesMarcados

    def set_golesMarcados(self, nuevosGoles):
        self._golesMarcados = nuevosGoles

    # Getter y Setter para tarjetasRojas
    def get_tarjetasRojas(self):
        return self._tarjetasRojas

    def set_tarjetasRojas(self, nuevasTarjetas):
        self._tarjetasRojas = nuevasTarjetas

    # Getter y Setter para piernaHabil
    def get_piernaHabil(self):
        return self._piernaHabil

    def set_piernaHabil(self, nuevaPierna):
        self._piernaHabil = nuevaPierna
        
        
    def __str__(self):
        return f"Mi nombre es {self.get_nombre()}, soy profesional en el deporte {self.get_deporte()}, tengo {self.get_edad()} años de edad y llevo {self.get_añosPracticando()} años en el deporte."