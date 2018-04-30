# Prueba del Programa 2.14: programa2_14Prueba.py 
# Prueba del programa de implementacion de una cola doblemente terminada en Python

from programa2_14 import *

d = ColaDoble()
print d.estaVacia()
d.agregarFinal(4)
d.agregarFinal('perro')
d.agregarFrente('gato')
d.agregarFrente(True)
print d.tamano()
print d.estaVacia()
d.agregarFinal(8.4)
print d.removerFinal()
print d.removerFrente()
print d.tamano()

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales