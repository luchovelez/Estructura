# Prueba del Programa 2.13: programa2_13Prueba.py 
# Programa de simulacion de cola de la impresora - Prueba de la simulacion principal

from programa2_13 import *

print 'Simulacion para un periodo de 60 minutos y una tasa de impresion de 5 paginas por minuto'
for i in range(10):
    simulacion(3600,5)
    
print 'Simulacion para un periodo de 60 minutos y una tasa de impresion de 10 paginas por minuto'    
for i in range(10):
    simulacion(3600,10)    

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales