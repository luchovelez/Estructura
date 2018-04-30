import string
import copy

class Field(object):
    
    def __init__(self, field):

   
        assert isinstance(field, list)
        self._field = field

        # inicializar alto y ancho
        self.height = len(field)
        self.width = len(field[0]) if self.height > 0 else 0

        # valida si todas las filas tiene el mismo tamaño
        for row in self._field:
            if len(row) != self.width:
                raise ValueError('valor de fila incorrecto %d != %d: %r' \
                            % (self.width, len(row), row))

        # valida caracteres
        for row in self._field:
            for cell in row:
                if cell not in ('.', '*'):
                    raise ValueError('solo punto (.) and asterisco (*)'
                                     'se esperan. se encontro %r ' % cell)

    def is_empty(self):
        """
        retorna True si el campo no tiene filas o columnas
        
        """
        return self.height == 0 or self.width == 0

    def is_bomb(self, i, j):
        """
        revisa si el indice dado es una bomba
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            return self._field[i][j] == '*'
        else:
            raise IndexError('indeice incorrecto (%d, %d)' % (i, j))

    def find_bombs(self):
        """
        muestra el indice de bombas (tuple)
        """
        for (i, row) in enumerate(self._field):
            for (j, cell) in enumerate(row):
                if cell == '*':
                    yield (i, j)

        # no index found
        raise StopIteration

    def find_adjacents(self, i, j):
        """
        muestra indice de adyacencia
        """
        # Comprueba si el índice de la celda existe
        # - indice negativo
        # - fuera del limite
        if 0 <= i < self.height and 0 <= j < self.width:
            # caminar sobre todos los indices de alrededor
            # Note: xrange genera i-1 <= m < i+2
            for m in xrange(i-1, i+2):
                for n in xrange(j-1, j+2):
                    if 0 <= m < self.height and 0 <= n < self.width \
                        and (m, n) != (i, j): 
                        yield (m, n)

        raise StopIteration
        
        
    def count_adjacents_bombs(self, i, j):
        """
        Regresa el total del conteo de bombas adyacentes
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            return sum(1 for (m, n) in self.find_adjacents(i, j)
                        if self.is_bomb(m,n))
        else:
            raise IndexError('Invalid index (%d, %d)' % (i, j))

    def resolve(self):
        """
        retorna la solucion del campo
        """
        result = copy.copy(self._field)
        for i in xrange(self.height):
            for j in xrange(self.width):
                if not self.is_bomb(i, j):
                    result[i][j] = str(self.count_adjacents_bombs(i, j))

        return result


    


listaCampo=[]
dimensiones =  raw_input()
lista=dimensiones.split(' ')
ancho=int(lista[0])
alto=int(lista[1])
matriz=[]
for i in range(alto):
    matriz.append([])
    for j in range(ancho):
        matriz[i].append('.') 
        
#~ print matriz



for i in range(alto):
     entrada=raw_input()
     for j in range(ancho):
            matriz[i][j]=entrada[j]
        
minas=Field(matriz)
salida= minas.resolve()
for i in salida:
    print ''.join(i)