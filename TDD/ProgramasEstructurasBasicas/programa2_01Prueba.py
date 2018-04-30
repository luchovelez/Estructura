# Prueba del Programa 2.1: programa2_01Prueba.py 
#  Prueba de la implementacion de una pila en Python, asumiendo que el tope esta al final de la lista
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01

p = Pila()
print p.estaVacia()
p.incluir(4)
p.incluir('perro')
print p.inspeccionar()
p.incluir(True)
print p.tamano()
print p.estaVacia()
p.incluir(8.4)
print p.extraer()
print p.extraer()
print p.tamano()

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
