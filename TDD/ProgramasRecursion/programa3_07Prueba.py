# Prueba del Programa 3.7: programa3_07Prueba.py 
# Prueba del programa del triangulo de Sierpinski


from programa3_07 import *
from time import *
ventana = GraphWin("Triangulo de Sierpinski", 500, 500)
puntos = [Point(50,450), Point(450, 450), Point(250,50)]
nivel = 3
sierpinskiT(puntos,nivel,ventana)
sleep(5)


# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales