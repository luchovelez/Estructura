# Programa 5.17: programa5_17.py 
# Clase de arbol binario de busqueda

from programa5_18 import *

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.tamano = 0
    
    def poner(self,clave,valor):
        if self.raiz:
            self.raiz.poner(clave,valor)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def __setitem__(self,c,v):
        self.poner(c,v)

    def obtener(self,clave):
        if self.raiz:
            return self.raiz.obtener(clave)
        else:
            return None

    def __getitem__(self,clave):
        return self.obtener(clave)

    def tiene_clave(self,clave):
        if self.raiz.obtener(clave):
            return True
        else:
            return False

    def longitud(self):
        return self.tamano
        
    def __len__(self):
        return self.tamano

    def borrar_clave(self,clave):
        if self.tamano > 1:
            self.raiz.borrar_clave(clave)
            self.tamano = self.tamano-1
        elif self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            print 'error, clave incorrecta'
            

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 