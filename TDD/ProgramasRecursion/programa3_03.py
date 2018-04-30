# Programa 3.3: programa3_03.py 
#  Convertir un entero a una cadena en base 2-16

cadenaConversion = "0123456789ABCDEF"

def aCadena(n,base):
   if n < base:              return cadenaConversion[n]
   else:
      return aCadena(n / base,base) + cadenaConversion[n%base]
      
# Asignatura de Estructuras de Datos
# Dr. Ing. Mauricio Orozco Alzate
# Departamento de Informatica y Computacion
# Universidad Nacional de Colombia Sede Manizales 