# Prueba de los Programas 5.17 y 5.18: programa5_17_18Prueba.py 
# Prueba del programa de arbol binario de busqueda

from programa5_17 import *
from programa5_18 import *

codigosSIA = ArbolBinarioBusqueda()
codigosSIA.poner('Estructuras de datos',4100548)
codigosSIA.poner('Mineria de datos',4101392)
codigosSIA.poner('Programacion 2',4100547)

print codigosSIA.obtener('Estructuras de datos')
print codigosSIA.obtener('Mineria de datos')
print codigosSIA.obtener('Programacion 2')

codigo = codigosSIA['Estructuras de datos']
print codigo

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales     
