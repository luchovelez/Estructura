# Programa 5.2: programa5_02.py 
# Funcion para insertar un subarbol izquierdo

def insertarIzquierdo(raiz,nuevaRama):
    t = raiz.pop(1)
    if len(t) > 1:
        raiz.insert(1,[nuevaRama,t,[]])
    else:
        raiz.insert(1,[nuevaRama, [], []])
    return raiz

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
