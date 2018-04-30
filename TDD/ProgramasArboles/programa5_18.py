# Programa 5.18: programa5_18.py 
# Clase NodoArbol

class NodoArbol:
    # Programa 5.18
    def __init__(self,clave,valor,padre=None, izquierdo=None,derecho=None):
        self.clave = clave
        self.carga = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
    
    # Programa 5.19
    def poner(self,clave,valor):
        if clave < self.clave:
            if self.hijoIzquierdo:
                self.hijoIzquierdo.poner(clave,valor)
            else:
                self.hijoIzquierdo = NodoArbol(clave,valor,self)
        else:
            if self.hijoDerecho:
                self.hijoDerecho.poner(clave,valor)
            else:
                self.hijoDerecho = NodoArbol(clave,valor,self)
    
    # Programa 5.20   
    def __setitem__(self,clave,valor):
        self.poner(clave,valor)
    
    # Programa 5.21    
    def obtener(self,clave):
        if clave == self.clave:
            return self.carga
        elif clave < self.clave:
            if self.hijoIzquierdo:
                return self.hijoIzquierdo.obtener(clave)
            else:
                return None
        elif clave > self.clave:
            if self.hijoDerecho:
                return self.hijoDerecho.obtener(clave)
            else:
                return None
        else:
            print 'error: this line should never be executed'
    
    def __getitem__(self,clave):
        return self.obtener(clave)

    # Programa 5.22
    #def longitud(self):
    #   return self.size
        
    #def __len__(self):
     #   return self.size

    
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Componeracion
# Universidad Nacional de Colombia Sede Manizales     
