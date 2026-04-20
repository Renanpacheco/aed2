'''Acesso Direto: Demonstre a eficiência O(1). Crie uma função que receba o vetor e
retorne a temperatura da "hora agendada" pelo usuário sem percorrer o array'''

import random
vetor = [round(random.random()*10) for _ in range(24)]

print(vetor)

def retornaValor(vetor, hora)->int:
    return vetor[hora]

h=input("qual hora quer verificar?")

print(retornaValor(vetor, int(h)))