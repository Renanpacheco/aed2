teste=["a", "b", "c", "d", "e"]
teste2=[]
def gerar_permuta(lista):
    
    if not lista:
        print("sem lista")
        return 0
    
    quadrado=2**len(lista)
    print(f"Total de combinações:{quadrado} ")
    #permuta = dict()
    #tupla = ()
    vetor=[]
    temp=0
    controle=1
    valores=[]
    
    for i in range(len(lista)):
        temp=controle*2
        vetor.append(lista[i])
        #vetor.append(temp)
        valores.append(temp)
        controle =controle*2
    #print(vetor)
    #print(valores)
    for j in range(len(lista)):
        print("")
    

gerar_permuta(teste)
gerar_permuta(teste2)


'''
    for i in range(len(lista)):
        print(lista[i])
    
    for i in lista:
        print(i)
'''