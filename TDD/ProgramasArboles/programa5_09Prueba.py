# Prueba del Programa 5.9: programa5_09Prueba.py 
# Prueba del codigo para crear un arbol de analisis sintactico

from programa5_09 import *

r= construirArbolSintactico('(3+(4*5))')
print r.obtenerValorRaiz()
print r.obtenerHijoIzquierdo()
print r.obtenerHijoDerecho()

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 