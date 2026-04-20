'''Estouro de Capacidade: Crie um vetor de tamanho 5. Tente inserir 6 elementos
usando um contador manual. Quando o contador superar o tamanho, exiba a
mensagem: "Erro: Overflow de Memória"
Estratégia de Expansão: Ao detectar o erro do exercício anterior, o programa deve:
○ Criar um novo vetor com o dobro do tamanho (10).
○ Copiar os dados do vetor antigo para o novo.
○ Deletar o vetor antigo (ou deixar o Garbage Collector agir).'''

def criarVetor(vetor):
    tamanho = 2*len(vetor)
    novoVetor=[None]*tamanho
    for i in vetor:
        novoVetor[i]=i
    print(novoVetor)

vetor = [None] * 5
escolha = "s"
contador=0


while escolha != "n":
    if contador>len(vetor)-1:
        #print("Erro: Overflow de Memória")
        criarVetor(vetor)
        break
    vetor[contador]= contador
    print(contador)
    contador=contador+1
    escolha=input("digite n para parar")
    

