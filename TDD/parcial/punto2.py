class Circular(list):
    
    def __init__(self, sequence=[]):
        super(Circular, self).__init__(sequence)
        self.position = 0

    def current(self):
        return self[self.position]
            
    def next(self, n=1):
        self.position = (self.position + n) % len(self)
        return self[self.position]
        
    def prev(self, n=1):
        return self.next(-n)
        
def evalturing(entrada):
    lista=[]
    for i in range(0,31):
        lista.append(i)
    turing = Circular(lista)
    #~ print lista
    for i in entrada:
        if i == ">":
            turing.next()
        if i == "<":
            turing.prev()
        if i == "#":
            print turing.current(),

entrada = raw_input()
print entrada
evalturing(entrada)

#~ evalturing('>>>#<<<<<#')
#~ print ''
#~ evalturing('>>>#>>><<#<<<#')
        
        
