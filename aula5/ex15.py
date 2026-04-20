'''Merge de Ordenados: Dados dois vetores A e B já ordenados, crie o vetor C que
combina ambos mantendo a ordem, sem usar o comando .sort().'''


A=[0,2,4,6]
B=[1,3,5,7]

tamanho= len(A)+len(B)
C=[None]*tamanho
aux=0
j=1

if A[0] < B[0]:
    for i in range(len(A)):
         C[i]=A[i]
    while j<len(B):
        if C[j]<=B[j]:
            j=j+1
        else:
            aux=C[j]
            C[j]=B[j]
            C[j+1]=aux
else:
    for i in range(len(B)):
         C[i]=B[i]
    while j<len(A):
        if C[j]<=A[j]:
            j=j+1
        else:
            aux=C[j]
            C[j]=A[j]
            C[j+1]=aux



print(C)
