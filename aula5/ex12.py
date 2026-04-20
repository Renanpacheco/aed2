'''Inversão In-Place: Inverta a ordem de todos os elementos do vetor sem criar um
vetor reserva. Use uma variável aux para trocar os elementos das extremidades até
chegar ao meio.'''
import random

def inverte(vetor):
    aux=0
    ultimo=len(vetor)-1
    for i in range(8):
        aux=vetor[i]
        vetor[i]=vetor[ultimo]
        vetor[ultimo]=aux
        ultimo=ultimo-1
    return vetor


vetor = [random.randint(1, 400) for _ in range(16)]
print(vetor)

inv= inverte(vetor)
print(inv)