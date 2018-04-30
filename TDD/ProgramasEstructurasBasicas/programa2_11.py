# Programa 2.11: programa2_11.py 
# Programa de simulacion de cola de la impresora - La clase Impresora
class Impresora:
    def __init__(self, paginas):
        self.tasaPaginas = paginas
        self.tareaActual = None
        self.tiempoRestante = 0

    def tictac(self):
        if self.tareaActual != None:
            self.tiempoRestante = self.tiempoRestante - 1
            if self.tiempoRestante == 0:
                self.tareaActual = None

    def ocupada(self):
        if self.tareaActual != None:
            return True
        else:
            return False

    def iniciarNueva(self,nuevaTarea):
        self.tareaActual = nuevaTarea
        self.tiempoRestante = nuevaTarea.obtenerPaginas() \
                             * 60/self.tasaPaginas

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
