valores = [10,5,2,7,15,12,20]

class Node():
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        

def inserir(raiz, valor):
    #print(raiz)
    if raiz is None:
        return Node(valor)
    elif valor < raiz.valor:
        raiz.esq= inserir(raiz.esq, valor)
        #return Node(inserir(raiz.esq, valor))
        #raiz.esq= Node(inserir(raiz.esq, valor))
    else:
        raiz.dir= inserir(raiz.dir, valor)
        #return Node(inserir(raiz.dir, valor))
        #raiz.dir= Node(inserir(raiz.esq, valor))
    return raiz

def preOrdem(raiz):
    if raiz is None:
        return
    print(raiz.valor)
    preOrdem(raiz.esq)
    preOrdem(raiz.dir)
        

def posOrdem(raiz):
    if raiz is None:
        return
    print(raiz.valor)
    preOrdem(raiz.dir)
    preOrdem(raiz.esq)    

tree= None

for i in valores:
   tree=inserir(tree,i)
   
print("pre ordem")
preOrdem(tree) 
print("pos ordem")
posOrdem(tree)