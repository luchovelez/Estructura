# Programa 2.7: programa2_07.py 
# Programa de conversion de expresiones Infix a expresiones Postfix
import string
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01

def infixAPostfix(expresionInfix):

    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1

    pilaOperadores = Pila()
    listaPostfix = []

    listaSimbolos = expresionInfix.split()

    for simbolo in listaSimbolos:
        if simbolo in string.uppercase:
            listaPostfix.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.incluir(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.extraer()
            while simboloTope != '(':
                listaPostfix.append(simboloTope)
                simboloTope = pilaOperadores.extraer()

        else:
            while (not pilaOperadores.estaVacia()) and \
               (precedencia[pilaOperadores.inspeccionar()] >= precedencia[simbolo]):
                  listaPostfix.append(pilaOperadores.extraer())

            pilaOperadores.incluir(simbolo)

    while not pilaOperadores.estaVacia():
        listaPostfix.append(pilaOperadores.extraer())

    return string.join(listaPostfix)

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
