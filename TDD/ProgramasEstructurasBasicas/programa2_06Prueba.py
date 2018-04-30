# Prueba del Programa 2.6: programa2_06Prueba.py 
# Prueba del programa de conversion de decimal a cualquier base (maximo base 16)
from programa2_06 import convertirBase

numeroDecimal = 233
cadenaOctal = convertirBase(numeroDecimal, 8)
cadenaHexadecimal = convertirBase(numeroDecimal, 16)
print 'El numero', numeroDecimal, 'en octal es ', cadenaOctal, 'y en hexadecimal es', cadenaHexadecimal

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales  
        