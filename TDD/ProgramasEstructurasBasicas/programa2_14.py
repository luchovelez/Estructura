# Programa 2.14: programa2_14.py 
# Programa de implementacion de una cola doblemente terminada en Python

class ColaDoble:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0,item)

    def removerFrente(self):
        return self.items.pop()

    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
