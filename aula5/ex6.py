'''Análise de Extremos: Implemente uma função que encontre o maior e o menor
valor do vetor percorrendo-o apenas uma vez (Complexidade O(n)).'''
import random

def encontrarMaiorMenor(vetor):
    maior=vetor[0]
    menor=vetor[0]
    for i in vetor:
        if i> maior:
            maior=i
        elif i< menor:
            menor=i
    
    print(f"maior= {maior} e menor = {menor}")
    
    

vetor = [round(random.random()*10) for _ in range(24)]
print(vetor)
encontrarMaiorMenor(vetor)