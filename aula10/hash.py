
pdfs=["aula1.pdf", "aula2.pdf", "aula3.pdf", "aula4.pdf", "aula5.pdf"]


class hashTable:
    def __init__(self, size=5)-> None:
        self.size=size
        self.tabela =[[] for _ in range(size)]
    
    def _hash(self, key):
        return minhaHash(key) % self.size

def minhaHash(key):
    
    return    
