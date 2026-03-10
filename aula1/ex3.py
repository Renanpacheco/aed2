txt= "I text for use in area"

def reverse(text):
    control= len(text)-1
    pile= ""
    
    for i in range(len(text)):
        #print(text.pop())
        aux= text[control-i]
        pile= pile + aux
    
    
    print(pile)

reverse(txt)

#tentar fazer transformando a string em um array e ir dando text.pop() um elemento por vez e mostrando na tela