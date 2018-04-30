# Prueba del Programa 2.3: programa2_03Prueba.py 
# Prueba del programa para solucionar el problema de verificacion de parentesis balanceados
from programa2_03 import verificarParentesis 

verificacion = verificarParentesis('(k)()()())')
if verificacion:
    print 'Los parentesis estan balanceados'
else:
    print 'Los parentesis no estan balanceados'

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales  
        