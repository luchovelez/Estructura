# Programa 5.3: programa5_03.py 
# Funcion para insertar un subarbol derecho

def insertarDerecho(raiz,nuevaRama):
    t = raiz.pop(2)
    if len(t) > 1:
        raiz.insert(2,[nuevaRama,[],t])
    else:
        raiz.insert(2,[nuevaRama,[],[]])
    return raiz
    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 
