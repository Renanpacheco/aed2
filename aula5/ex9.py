'''Estouro de Capacidade: Crie um vetor de tamanho 5. Tente inserir 6 elementos
usando um contador manual. Quando o contador superar o tamanho, exiba a
mensagem: "Erro: Overflow de Memória"
Estratégia de Expansão: Ao detectar o erro do exercício anterior, o programa deve:
○ Criar um novo vetor com o dobro do tamanho (10).
○ Copiar os dados do vetor antigo para o novo.
○ Deletar o vetor antigo (ou deixar o Garbage Collector agir).
 Relatório de Overhead: A cada inserção, imprima: Itens: X | Capacidade Real: Y.
Observe como a capacidade aumenta em saltos, e não um a um.'''

def criarVetor(vetor):
    tamanho = 2*len(vetor)
    novoVetor=[None]*tamanho
    for i in vetor:
        novoVetor[i]=i
    print(novoVetor)

vetor = [None] * 5
escolha = "s"
contador=0


while escolha == "s":
    if contador>len(vetor)-1:
        
        criarVetor(vetor)
        break
    vetor[contador]= contador
    print(f"Itens: {contador+1} | Capacidade Real: {len(vetor)-contador}")
    contador=contador+1
    escolha=input("digite s para continuar ")
    

