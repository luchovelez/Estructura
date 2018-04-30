# Programa 3.2: programa3_02.py 
#  Funcion de suma recursiva

def sumaLista(l):
    if len(l) == 1:                       return l[0]
    else:
        return l[0] + sumaLista(l[1:]) 
            
 # Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 