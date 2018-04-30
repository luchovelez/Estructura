# Programa 5.11: programa5_11.py 
# Funcion externa que implementa el recorrido de un arbol en preorden

def preorden(arbol):
    if arbol:
        print arbol.obtenerValorRaiz()        
        preorden(arbol.obtenerHijoIzquierdo())
        preorden(arbol.obtenerHijoDerecho())  


# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 