# Programa 2.10: programa2_10.py 
# Programa de simulacion del juego de la papa caliente
from programa2_09 import *

def papaCaliente(listaNombres, N):

    colaSimulacion = Cola()
    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)

    while colaSimulacion.tamano() > 1:
        for i in range(N):
            colaSimulacion.agregar(colaSimulacion.avanzar())

        colaSimulacion.avanzar()

    return colaSimulacion.avanzar()

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
