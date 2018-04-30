# Programa 2.3: programa2_03.py 
# Programa para solucionar el problema de verificacion de parentesis balanceados
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01


def verificarParentesis(cadenaSimbolos):
    p = Pila()
    
    balanceados = True # Se asume inicialmente que los parentesis estan balanceados
    indice = 0

    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo == "(":
            p.incluir(simbolo)
        else: 
            if p.estaVacia():
                balanceados = False
            else:
                p.extraer()

        indice = indice + 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False
        
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 