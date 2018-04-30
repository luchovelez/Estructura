# Programa 5.5-5-8: programa5_05_08.py 
# Definicion de la clase ArbolBinario

class ArbolBinario:
    def __init__(self,objetoRaiz):
        self.clave = objetoRaiz
        self.izquierda = None
        self.derecha = None
    
    # Insercion de un nuevo hijo izquierdo    
    def insertarIzquierda(self,nuevoNodo):
        if self.izquierda == None:
            self.izquierda = ArbolBinario(nuevoNodo)
        else:               
            t = ArbolBinario(nuevoNodo)
            t.izquierda = self.izquierda
            self.izquierda = t    
    
    # Insercion de un nuevo hijo derecho
    def insertarDerecha(self,nuevoNodo):
        if self.derecha == None:
            self.derecha = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.derecha = self.derecha
            self.derecha = t
    
    # Metodos de acceso para la Clase ArbolBinario
    def obtenerValorRaiz(self,):
        return self.clave

    def asignarValorRaiz(self,obj):
        self.clave = obj

    def obtenerHijoIzquierdo(self):
        return self.izquierda

    def obtenerHijoDerecho(self):
        return self.derecha
            
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 