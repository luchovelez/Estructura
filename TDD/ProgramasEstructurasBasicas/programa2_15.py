# Programa 2.15: programa2_15.py 
# Programa de verificacion de palindromos

from programa2_14 import *

def verificarPalindromo(cadena):
    
    colaDobleCaracteres = ColaDoble()
    for  caracter in cadena:
        colaDobleCaracteres.agregarFinal(caracter)
    
    aunIguales = True
    
    while colaDobleCaracteres.tamano() > 1 and aunIguales:
        primero = colaDobleCaracteres.removerFrente()
        ultimo = colaDobleCaracteres.removerFinal()
        if primero != ultimo:
            aunIguales = False

    return aunIguales

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales
