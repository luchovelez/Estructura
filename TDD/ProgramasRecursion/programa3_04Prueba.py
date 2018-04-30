# Prueba del Programa 3.4: programa3_04Prueba.py 
#  Prueba de la funcion para  convertir un entero a una cadena en base 2-16 (con incluision de las cadenas en una pila)
from programa3_04 import * # Importar la funcion de suma recursiva

numero = 769
base = 8

pilaCadena = aCadena(numero,base)

print 'El numero', numero, 'convertido a base', base, 'es', 
for i in range(pilaCadena.tamano()):
    print pilaCadena.extraer(),
    
 # Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
