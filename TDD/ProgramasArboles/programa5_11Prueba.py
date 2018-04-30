# Prueba del Programa 5.11: programa5_11Prueba.py 
# Prueba de la funcion externa que implementa el recorrido de un arbol en preorden

from programa5_05_08 import *
from programa5_11 import *
from programa5_13 import *
from programa5_15 import *

#libro = ArbolBinario('Libro')
#libro.insertarIzquierda('Seccion 1.1')
#libro.insertarIzquierda('Capitulo 1')
#libro.obtenerHijoIzquierdo().insertarDerecha('Seccion 1.2.2')
#libro.obtenerHijoIzquierdo().insertarDerecha('Seccion 1.2')
#seccion1_2 = libro.obtenerHijoIzquierdo().obtenerHijoDerecho()
#seccion1_2.insertarIzquierda('Seccion 1.2.1')

raiz = ArbolBinario(13)
raiz.insertarIzquierda(1)
raiz.insertarIzquierda(3)
raiz.insertarDerecha(18)
raiz.insertarDerecha(14)
c = raiz.obtenerHijoIzquierdo()
c.insertarDerecha(12)
c.insertarDerecha(4)
d = c.obtenerHijoIzquierdo()
d.insertarDerecha(2)
e = c.obtenerHijoDerecho().obtenerHijoDerecho()
e.insertarIzquierda(10)
f = e.obtenerHijoIzquierdo()
f.insertarDerecha(11)
f.insertarIzquierda(5)
g = f.obtenerHijoIzquierdo()
g.insertarDerecha(9)
g.insertarDerecha(8)
h = g.obtenerHijoDerecho()
h.insertarIzquierda(6)
h.insertarIzquierda(7)

# Recorrido en preorden
print 'Recorrido en preorden:'
preorden(raiz)
print ''
print 'Recorrido en postorden:'
postorden(raiz)
print ''
print 'Recorrido en inorden:'
inorden(raiz)


# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 