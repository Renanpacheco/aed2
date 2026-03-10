number=input("enter a number: ")
#print(type(number))
even=0
aux=0

for letter in number:
    aux= int(letter)
    if aux % 2 == 0 :
        even = even+1

print(even)