'''Busca Manual: Implemente uma função existeTemperatura(vetor, valorBuscado).
Use um laço para percorrer o vetor e retorne o índice da primeira ocorrência. Se não
encontrar, retorne -1.'''
import random

def existeTemperatura(vetor, valorBuscado)-> int:
    for i in range(len(vetor)):
        if vetor[i] == valorBuscado:
            return i
    return -1

vetor = [round(random.random()*10) for _ in range(24)]
print(vetor)

horas =existeTemperatura(vetor, 9)    
if horas >= 0:
    print(f"A temperatura ocorreu a primeira vez as {horas}h")
else:
    print("temperatura não encontrada")