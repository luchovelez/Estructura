# Programa 5.10: programa5_10.py 
# Funcion recursiva para evaluar un arbol de analisis sintactico binario

import operator # Modulo

def evaluar(arbolSintactico):
    operadores = {'+':operator.add, '-':operator.sub,'*':operator.mul, '/':operator.div}
    hijoIzquierda = arbolSintactico.obtenerHijoIzquierdo()
    hijoDerecha = arbolSintactico.obtenerHijoDerecho()
        
    if hijoIzquierda and hijoDerecha:
        fn = operadores[arbolSintactico.obtenerValorRaiz()]
        return fn(evaluar(hijoIzquierda),evaluar(hijoDerecha))
    else:
        return arbolSintactico.obtenerValorRaiz()

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 