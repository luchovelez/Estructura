# Prueba del Programa 2.7: programa2_07.py 
# Prueba del programa de conversion de expresiones Infix a expresiones Postfix
import string
from programa2_07 import *

print infixAPostfix("( A + B ) * ( C + D )")
print infixAPostfix("( A + B ) * C")
print infixAPostfix("A + B * C")

print infixAPostfix("( ( ( ( A + B ) * ( C + D + E ) + F ) * G ) + H )")
print infixAPostfix("A * B * C / D - ( E + F )")
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
