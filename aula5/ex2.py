'''Remoção com Compactação: Crie uma função removerDaPosicao(vetor, indice).
Após apagar o dado, mova todos os elementos à direita para a esquerda, garantindo
que não fiquem "buracos" (valores nulos/undefined) no meio do vetor.'''

def removerDaPosicao(vetor, indice):
    i=indice
    while i<len(vetor)-1:
        vetor[i]=vetor[i+1]
        i=i+1
    
    vetor[9]=None
        

vetor = [0,1,2,3,4,5,6,7,8,9]

removerDaPosicao(vetor,5)
print(vetor)