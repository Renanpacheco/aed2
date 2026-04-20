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
