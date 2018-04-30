# Programa 2.2: programa2_02.py 
#  Implementacion alternativa de una pila en Python, asumiendo que el tope esta al principio de la lista
# Nota: comparar con la implementacion en el Programa 2.1
class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.insert(0, item) # Insertar en la posicion 0 en lugar de usar append

    def extraer(self):
        return self.items.pop(0) # Usar pop explicitando la posicion 0

    def inspeccionar(self):
        return self.items[0] # Inspeccionar el item de la posicion 0

    def tamano(self):
        return len(self.items)
        
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
