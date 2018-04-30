# Programa 5.9: programa5_09.py 
# codigo para crear un arbol de analisis sintactico

from programa2_01 import Pila # Importar la clase Pila del modulo programa2_01
from programa5_05_08 import ArbolBinario # Importar la clase ArbolBinario del modulo programa5_05_08

def construirArbolSintactico(expresion):
    listaExpresion = expresion.split()
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    for i in listaExpresion:
        if i == '(': 
            arbolActual.insertarIzquierda('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in '+-*/)':              
            arbolActual.asignarValorRaiz(eval(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in '+-*/':
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecha('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()      
        elif i == ')':                      
            arbolActual = pilaPadres.extraer()
        else:
            print "error:  no se reconoce " + i
    return arbolExpresion

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 