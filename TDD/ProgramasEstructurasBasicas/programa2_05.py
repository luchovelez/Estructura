# Programa 2.5: programa2_05.py 
# Programa de conversion de decimal a binario
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01

def dividirPor2(numeroDecimal):

    pilaResiduo = Pila()

    while numeroDecimal > 0:
        residuo = numeroDecimal % 2
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal / 2

    cadenaBinaria = ""
    while not pilaResiduo.estaVacia():
        cadenaBinaria = cadenaBinaria + str(pilaResiduo.extraer())

    return cadenaBinaria
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
