# Programa 2.8: programa2_08.py 
# Programa de evaluacion de Postfix
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01

def evaluacionPostfix(expresionPostfix):

    pilaOperandos = Pila()

    listaSimbolos = expresionPostfix.split()

    for simbolo in listaSimbolos:
        if simbolo in "0123456789":
            pilaOperandos.incluir(int(simbolo))
        else:
            operando2 = pilaOperandos.extraer()
            operando1 = pilaOperandos.extraer()
            resultado = hacerAritmetica(simbolo,operando1,operando2)
            pilaOperandos.incluir(resultado)

    return pilaOperandos.extraer()

def hacerAritmetica(op, op1, op2):
    if op == "*":
        return op1 * op2
    else:
        if op == "/":
            return op1 / op2
        else:
            if op == "+":
                return op1 + op2
            else:
                return op1 - op2

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
