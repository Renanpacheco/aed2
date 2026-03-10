#Remover Elementos Negativos de Lista Dado um vetor/lista de inteiros, escreva um algoritmo que retorna uma nova lista apenas com os números não-negativos.

lis=[2,-1,4,6,-5,0]

positives=[]

for i in range(len(lis)):
    if lis[i]>=0:
        positives.append(lis[i])
        
print(positives)

orderedList= sorted(lis)
print(orderedList)

#def positives(array)t:
    
while orderedList[0] < 0:
    orderedList.pop(0)

print(orderedList)