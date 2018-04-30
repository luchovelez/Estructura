# Prueba de los Programas 5.1 a 5.4: programa5_01-04Prueba.py 
# Programa para ilustrar las funciones basicas de con arboles

from programa5_01 import *
from programa5_02 import *
from programa5_03 import *
from programa5_04 import *

r = ArbolBinario(3)
print insertarIzquierdo(r, 4)
print insertarIzquierdo(r, 5)
print insertarDerecho(r, 6)
print insertarDerecho(r, 7)
l = obtenerHijoIzquierdo(r)
print l
asignarValorRaiz(l,9)
print r
print insertarIzquierdo(l, 11)
print r


# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 