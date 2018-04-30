# Programa 2.13: programa2_13.py 
# Programa de simulacion de cola de la impresora - La simulacion principal

from programa2_09 import * # Importar la clase Cola
from programa2_11 import * # Importar la clase Impresora
from programa2_12 import * # Importar la clase Tarea

import random

def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

      if nuevaTareaImpresion():
         tarea = Tarea(segundoActual)
         colaImpresion.agregar(tarea)

      if (not impresoraLaboratorio.ocupada()) and \
                (not colaImpresion.estaVacia()):
        tareaSiguiente = colaImpresion.avanzar()
        tiemposEspera.append( \
            tareaSiguiente.tiempoEspera(segundoActual))
        impresoraLaboratorio.iniciarNueva(tareaSiguiente)

      impresoraLaboratorio.tictac()

    esperaPromedio=sum(tiemposEspera)/float(len(tiemposEspera))
    print "Tiempo de espera promedio%6.2f segundos"%(esperaPromedio),
    print "Tareas restantes %3d"%(colaImpresion.tamano())


def nuevaTareaImpresion():
    numero = random.randrange(1,181)
    if numero == 180:
        return True
    else:
        return False

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales