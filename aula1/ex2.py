text= "I text for use in area"
aux= ""

text= text.lower()

for letter in text:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        #text.replace(letter, "*")
        aux=aux+ "*"
    else:
        aux=aux+letter
        
print(text)
print(aux)