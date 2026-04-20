'''Estouro de Capacidade: Crie um vetor de tamanho 5. Tente inserir 6 elementos
usando um contador manual. Quando o contador superar o tamanho, exiba a
mensagem: "Erro: Overflow de Memória"'''

vetor = [None] * 5
escolha = "s"
contador=0

while escolha != "n":
    if contador>4:
        print("Erro: Overflow de Memória")
        break
    vetor[contador]= contador
    print(contador)
    contador=contador+1
    escolha=input("digite n para parar")
    

