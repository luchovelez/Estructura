# Prueba del Programa 5.16: programa5_16Prueba.py 
# codigo para crear un arbol de analisis sintactico
from programa5_05_08 import *
from programa5_16 import *

x = ArbolBinario('*')
x.insertarIzquierda('+')
l = x.obtenerHijoIzquierdo()
l.insertarIzquierda(4)
l.insertarDerecha(5)
x.insertarDerecha(7)
print imprimirExpresion(x)

    
    # Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
