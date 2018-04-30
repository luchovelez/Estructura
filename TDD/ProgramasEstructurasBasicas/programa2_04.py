# Programa 2.4: programa2_04.py 
# Programa para solucionar el problema de verificacion de simbolos balanceados
from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01
def verificarSimbolos(cadenaSimbolos):

    p = Pila()

    balanceados = True
    indice = 0

    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo in "([{":
            p.incluir(simbolo)
        else:
            if p.estaVacia():
                balanceados = False
            else:
                tope = p.extraer()
                if not parejas(tope,simbolo):
                       balanceados = False

        indice = indice + 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False

def parejas(apertura,cierre):
    aperturas = "([{"
    cierres = ")]}"

    return aperturas.index(apertura) == cierres.index(cierre)
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
