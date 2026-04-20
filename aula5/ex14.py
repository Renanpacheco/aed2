'''Unique (Sem Set): Dado um vetor com valores repetidos e ordenados (ex: [1, 1, 2,3, 3]), 
remova as duplicatas deslocando os elementos para a esquerda, deixando o vetor "limpo".'''


def unique(vetor):
    aux=vetor[0]
    #tamanho=len(vetor)
    contador =0
    controle=1
    while controle < 4:
        if aux != vetor[controle]:
            vetor[controle]=vetor[controle+1]
            controle=controle+1
            
        else:
            controle=controle+1
            aux=vetor[controle]
            
        
    return vetor


vetor = [1, 1, 2,3, 3]
print(vetor)

inv= unique(vetor)
print(inv)

'''def merge(vetor1, vetor2):
    tamanho= len(vetor1)+len(vetor2)
    temp=[None]*tamanho
    aux=0
    for i in range(tamanho-1):
        #if vetor1[i] < vetor2[i]:
           # aux
        while vetor1[i] < vetor2[i]:
            
            temp[aux]=vetor1[aux]
        temp[aux]=vetor2[i]
    return temp
'''

'''for i in range(len(vetor1)-1):
        #if vetor1[i] < vetor2[i]:
           # aux
    while vetor1[i] < vetor2[j]:
        temp[aux]=vetor1[aux]
        aux=aux+1
        j=j+1
    j=i
        
    temp[aux]=vetor2[i]
'''