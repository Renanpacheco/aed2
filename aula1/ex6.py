def conj(lis):
    thisSet=set()
    temp=0
    for i in range(len(lis)):
        temp= lis[i]
        thisSet.add(temp)
    #print(thisSet)
    return thisSet   
    
    


vector= [1,2,3,1,2,3,4,4]
newSet=conj(vector)
print(newSet)