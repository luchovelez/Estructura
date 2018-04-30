# Programa 3.4: programa3_04.py 
#  Convertir un entero a una cadena en base 2-16 (con incluision de las cadenas en una pila)
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01

convertirCadena = "0123456789ABCDEF"
pilaR = Pila()

def aCadena(n,base):
    if n < base:                 
        pilaR.incluir(convertirCadena[n])
    else:
        pilaR.incluir(convertirCadena[n%base])
        aCadena(n / base,base)  
    return pilaR
    
 # Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 