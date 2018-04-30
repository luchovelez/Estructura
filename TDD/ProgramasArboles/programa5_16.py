# Programa 5.16: programa5_16.py 
# codigo para crear un arbol de analisis sintactico

def imprimirExpresion(arbol):
    expresionAgrupada = ""
    if arbol:
        expresionAgrupada = '(' + imprimirExpresion(arbol.obtenerHijoIzquierdo())
        expresionAgrupada = expresionAgrupada + str(arbol.obtenerValorRaiz())
        expresionAgrupada = expresionAgrupada + imprimirExpresion(arbol.obtenerHijoDerecho())+')'
    return expresionAgrupada
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
