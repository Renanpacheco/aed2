''' Filtro de Contraste: Percorra o vetor de pixels e multiplique cada valor por 1.2. Se o
resultado for maior que 255, force o valor para 255 (Truncamento).'''

import random

vetor = [random.randint(0, 255) for _ in range(16)]

print(vetor)


for i in range(len(vetor)):
    vetor[i]=vetor[i]*1.2
    if vetor[i] > 255:
        vetor[i]=255

print(vetor)