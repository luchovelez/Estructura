# Prueba de los Programas 5.11, 5.13 y 5.15: programa5_11_13_15Prueba.py 
# Prueba de la funcion externa que implementa el recorrido de un arbol en preorden

from programa5_05_08 import *
from programa5_11 import *
from programa5_13 import *
from programa5_15 import *

libro = ArbolBinario('Libro')
libro.insertarIzquierda('Seccion 1.1')
libro.insertarIzquierda('Capitulo 1')
libro.obtenerHijoIzquierdo().insertarDerecha('Seccion 1.2.2')
libro.obtenerHijoIzquierdo().insertarDerecha('Seccion 1.2')
libro.obtenerHijoIzquierdo().obtenerHijoDerecho().insertarIzquierda('Seccion 1.2.1')
libro.insertarDerecha('Seccion 2.2.2')
libro.insertarDerecha('Seccion 2.2')
libro.insertarDerecha('Capitulo 2')
libro.obtenerHijoDerecho().insertarIzquierda('Seccion 2.1')
libro.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierda('Seccion 2.2.1')



# Recorrido en preorden
print 'Recorrido en preorden:'
preorden(libro)
print ''
print 'Recorrido en postorden:'
postorden(libro)
print ''
print 'Recorrido en inorden:'
inorden(libro)


# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 