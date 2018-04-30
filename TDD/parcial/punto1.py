from programa2_04 import verificarSimbolos
from programa2_01 import Pila
#~ entrada='((1-2)*3)[(4/7)))'
entrada=raw_input()
#~ print entrada
pagrupaccion = Pila()
poperadores = Pila()
poperandos = Pila()
listaagrupacion=""
listaoperadores=""
invalidez=True
#~ print entrada
for i in entrada:
    if  i.isdigit() or i not in '()[]{}':
        if poperadores.estaVacia():
             poperadores.incluir(i)
             listaoperadores = listaoperadores+i
        else:
            #~ print "nuevo " + i
            #~ print "viejo " + poperadores.inspeccionar()
            if  poperadores.inspeccionar() != i:
                poperadores.incluir(i)
            else:
                print "Incorrecto!"
                invalidez=True
                break
            
            #~ print listaoperadores
            listaoperadores = listaoperadores+i
            
                 
             
        #~ if poperadores.inspeccionar == i :
            #~ print 'error'
            #break
     
        
    if  not i.isdigit() and  i not in '+-*/':
        pagrupaccion.incluir(i)
        listaagrupacion = listaagrupacion+i
        
#~ print listaagrupacion
#~ print listaoperadores

verificacion = verificarSimbolos(listaagrupacion)
if verificacion  :
    print 'correcto!'
else:
    print 'Incorrecto!'
