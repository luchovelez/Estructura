# Programa 3.5: programa3_05.py 
# Programa para el problema de las torres de Hanoi

from programa3_06 import *

def moverTorre(altura,delPoste, alPoste, conPoste):
    if altura >= 1:
        moverTorre(altura-1,delPoste,conPoste,alPoste)
        moverDisco(delPoste,alPoste)
        moverTorre(altura-1,conPoste,alPoste,delPoste)
    

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales

