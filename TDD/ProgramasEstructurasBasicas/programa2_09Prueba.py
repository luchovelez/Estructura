# Prueba del Programa 2.9: programa2_09Prueba.py 
# Prueba del programa de implementacion de una cola en Python
from programa2_09 import *

c = Cola()
print c.estaVacia()
c.agregar('perro')
c.agregar(4)
c = Cola()
print c.estaVacia()
c.agregar(4)
c.agregar('perro')
c.agregar(True)
print c.tamano()
print c.estaVacia()
c.agregar(8.4)
print c.avanzar()
print c.avanzar()
print c.tamano()
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
