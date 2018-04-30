# Programa 2.12: programa2_12.py 
# Programa de simulacion de cola de la impresora - La clase Tarea
import random
class Tarea:
    def __init__(self,tiempo):
        self.marcaTiempo = tiempo
        self.paginas = random.randrange(1,21)

    def obtenerMarca(self):
        return self.marcaTiempo

    def obtenerPaginas(self):
        return self.paginas

    def tiempoEspera(self, tiempoActual):
        return tiempoActual - self.marcaTiempo
        
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
