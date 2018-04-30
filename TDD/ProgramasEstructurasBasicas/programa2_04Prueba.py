# Prueba del Programa 2.4: programa2_04Prueba.py 
# Prueba del programa para solucionar el problema de verificacion de simbolos balanceados
from programa2_04 import verificarSimbolos

verificacion = verificarSimbolos('{{([][])}()}')
if verificacion:
    print 'Los simbolos estan balanceados'
else:
    print 'Los simbolos no estan balanceados'

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales  
        