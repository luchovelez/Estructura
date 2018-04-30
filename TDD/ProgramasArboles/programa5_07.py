# Programa 5.7: programa5_07.py 
# Insercion de un nuevo hijo derecho
# Este metodo pertenece a la Clase ArbolBinario. Ver programa5_05_08.py

    def insertarDerecha(self,nuevoNodo):
        if self.derecha == None:
            self.derecha = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.derecha = self.derecha
            self.derecha = t

# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 