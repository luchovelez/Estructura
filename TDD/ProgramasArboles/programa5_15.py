# Programa 5.15: programa5_15.py 
# Funcion externa que implementa el recorrido de un arbol en inorden

def inorden(arbol):
    if arbol != None:
        inorden(arbol.obtenerHijoIzquierdo())
        print arbol.obtenerValorRaiz()
        inorden(arbol.obtenerHijoDerecho())
        
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales         
