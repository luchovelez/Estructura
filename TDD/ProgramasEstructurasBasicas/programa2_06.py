# Programa 2.6: programa2_06.py 
# Programa de conversion de decimal a cualquier base (maximo base 16)
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01

def convertirBase(numeroDecimal, base):

    digitos = "0123456789ABCDEF"

    pilaResiduo = Pila()

    while numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal / base

    nuevaCadena = ""
    while not pilaResiduo.estaVacia():
        nuevaCadena = nuevaCadena + digitos[pilaResiduo.extraer()]

    return nuevaCadena
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
