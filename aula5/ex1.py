'''1. Inserção em O(n): Crie uma função inserirNoInicio(vetor, novoPaciente). Você deve
percorrer o vetor do fim para o começo, movendo cada elemento uma posição para
a direita, e então inserir o novo paciente no índice 0.'''


def inserirNoInicio(vetor, novoPaciente):
    
    i=9
    
    while i>0:
        
        vetor[i]=vetor[i-1]
        i=i-1
    vetor[0]=novoPaciente
    print(vetor)
        
vetor = [None] * 10
inserirNoInicio(vetor, 1)
inserirNoInicio(vetor, 2)
inserirNoInicio(vetor, 3)
inserirNoInicio(vetor, 4)
inserirNoInicio(vetor, 5)
inserirNoInicio(vetor, 6)
inserirNoInicio(vetor, 7)
inserirNoInicio(vetor, 8)
inserirNoInicio(vetor, 9)
inserirNoInicio(vetor, 10)
inserirNoInicio(vetor, 11)
