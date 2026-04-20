''' Vetor Esparso: Escreva uma função que conte quantos elementos são "zero" em
um vetor de 50 posições. Se mais de 70% forem zero, imprima "Vetor Ineficiente:
Recomenda-se compressão" '''

import random

def esparso(vetor):
    cont=0
    setentaPorCento=len(vetor)*0.7
    for i in vetor:
        if i==0 :
            cont=cont+1
        
        if cont>=setentaPorCento :
            print("Vetor Ineficiente: Recomenda-se compressão")
            return
    print(cont)
    print("vetor OK")
    return


#vetor = [random.randint(0, 1) for _ in range(50)]
vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
print(vetor)

esparso(vetor)
