# Prueba del Programa 5.5-5.8: programa5_05-08Prueba.py 
# Programa para ilustrar el uso y manejo de la clase ArbolBinario

from programa5_05_08 import *

r = ArbolBinario('a')
print r.obtenerValorRaiz()
print r.obtenerHijoIzquierdo()
r.insertarIzquierda('b')
print r.obtenerHijoIzquierdo()
print r.obtenerHijoIzquierdo().obtenerValorRaiz()
r.insertarDerecha('c')
print r.obtenerHijoDerecho()
print r.obtenerHijoDerecho().obtenerValorRaiz()
r.obtenerHijoDerecho().asignarValorRaiz('hola')
print r.obtenerHijoDerecho().obtenerValorRaiz()

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 