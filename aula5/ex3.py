'''Contador de Custo: Altere as funções anteriores para que elas retornem, além do
vetor, o número de vezes que o computador precisou "mover" um dado na memória.
Compare o custo de inserir no índice 0 vs. inserir no último índice vago.'''

'''Inserção em O(n): Crie uma função inserirNoInicio(vetor, novoPaciente). Você deve
percorrer o vetor do fim para o começo, movendo cada elemento uma posição para
a direita, e então inserir o novo paciente no índice 0.'''


def inserirNoInicio(vetor, novoPaciente) -> int:
    cont=0
    i=9
    
    while i>0:
        
        vetor[i]=vetor[i-1]
        i=i-1
        cont= cont+1
    vetor[0]=novoPaciente
    print(vetor)
    return cont
        
vetor = [None] * 10
temp=inserirNoInicio(vetor, 1)
print(temp)
temp=inserirNoInicio(vetor, 2)
print(temp)
temp=inserirNoInicio(vetor, 3)
print(temp)
temp=inserirNoInicio(vetor, 4)
print(temp)
temp=inserirNoInicio(vetor, 5)
print(temp)
temp=inserirNoInicio(vetor, 6)
print(temp)
temp=inserirNoInicio(vetor, 7)
print(temp)
temp=inserirNoInicio(vetor, 8)
print(temp)
temp=inserirNoInicio(vetor, 9)
print(temp)
temp=inserirNoInicio(vetor, 10)
print(temp)
temp=inserirNoInicio(vetor, 11)
print(temp)

'''Remoção com Compactação: Crie uma função removerDaPosicao(vetor, indice).
Após apagar o dado, mova todos os elementos à direita para a esquerda, garantindo
que não fiquem "buracos" (valores nulos/undefined) no meio do vetor.'''

def removerDaPosicao(vetor, indice)->int:
    i=indice
    cont=0
    while i<len(vetor)-1:
        vetor[i]=vetor[i+1]
        i=i+1
        cont= cont+1
    
    vetor[9]=None
    return cont
    
        


temp= removerDaPosicao(vetor,5)
print(vetor)
print(temp)