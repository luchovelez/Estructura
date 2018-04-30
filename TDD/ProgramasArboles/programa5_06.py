# Programa 5.6: programa5_06.py 
# Insercion de un nuevo hijo izquierdo

# Este metodo pertenece a la Clase ArbolBinario. Ver programa5_05_08.py
    def insertarIzquierda(self,nuevoNodo):
        if self.izquierda == None:
            self.izquierda = ArbolBinario(nuevoNodo)
        else:               
            t = ArbolBinario(nuevoNodo)
            t.izquierda = self.izquierda
            self.izquierda = t

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 