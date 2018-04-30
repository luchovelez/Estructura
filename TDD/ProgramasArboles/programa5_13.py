# Programa 5.11: programa5_11.py 
# Funcion externa que implementa el recorrido de un arbol en preorden

def postorden(arbol):
    if arbol != None:
        postorden(arbol.obtenerHijoIzquierdo())
        postorden(arbol.obtenerHijoDerecho())
        print arbol.obtenerValorRaiz()

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
