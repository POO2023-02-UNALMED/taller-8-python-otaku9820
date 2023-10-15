class Deportista:
    def __init__(self,añosPracticando ):
        
        self._añosPracticando=añosPracticando
        self._deporte="futbol"
    
    def getDeporte(self):
        return self._deporte

    def setDeporte(self, nuevo_deporte):
        self._deporte = nuevo_deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self, nuevos_años):
        self._añosPracticando = nuevos_años    
        
        
        
    