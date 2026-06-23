ocorrencias = []

fila_atendimento = []

historico = []

indice_nome = {}
indice_tipo = {}


def gerar_id(nome):
    soma = 0

    for letra in nome:
        soma += ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def registrar_acao(acao):
    historico.append(acao)


def cadastrar_ocorrencia():
    print("\nCADASTRAR OCORRÊNCIA")

    nome = input("Nome do requisitante: ")
    id_ocorrencia = gerar_id(nome)

    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")
    prioridade = int(input("Prioridade (1 a 5): "))

    ocorrencia = {
        "id": id_ocorrencia,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "prioridade": prioridade
    }

    
    ocorrencias.append(ocorrencia)

    
    fila_atendimento.append(ocorrencia)

    
    if nome not in indice_nome:
        indice_nome[nome] = []

    indice_nome[nome].append(ocorrencia)

    if tipo not in indice_tipo:
        indice_tipo[tipo] = []

    indice_tipo[tipo].append(ocorrencia)

    registrar_acao(f"Cadastro da ocorrência {id_ocorrencia}")

    print("\nOcorrência cadastrada com sucesso!")
    print("ID:", id_ocorrencia)


def listar_ocorrencias():
    print("\nLISTA DE OCORRÊNCIAS")

    if not ocorrencias:
        print("Nenhuma ocorrência cadastrada.")
        return

    for oc in ocorrencias:
        print("---------------------")
        print("ID:", oc["id"])
        print("Nome:", oc["nome"])
        print("Tipo:", oc["tipo"])
        print("Prioridade:", oc["prioridade"])

    registrar_acao("Listagem de ocorrências")


def buscar_por_id():
    id_busca = input("Digite o ID: ")

    for oc in ocorrencias:
        if oc["id"] == id_busca:
            print("\nOcorrência encontrada:")
            print(oc)
            registrar_acao(f"Busca por ID {id_busca}")
            return

    print("Ocorrência não encontrada.")


def buscar_por_nome():
    nome = input("Nome: ")

    if nome in indice_nome:
        for oc in indice_nome[nome]:
            print(oc)
    else:
        print("Nenhuma ocorrência encontrada.")

    registrar_acao(f"Busca por nome {nome}")


def buscar_por_tipo():
    tipo = input("Tipo: ")

    if tipo in indice_tipo:
        for oc in indice_tipo[tipo]:
            print(oc)
    else:
        print("Nenhuma ocorrência encontrada.")

    registrar_acao(f"Busca por tipo {tipo}")


def atender_proxima_ocorrencia():
    print("\nATENDIMENTO")

    if not fila_atendimento:
        print("Fila vazia.")
        return

    ocorrencia = fila_atendimento.pop(0)

    print("Atendendo ocorrência:")
    print("ID:", ocorrencia["id"])
    print("Nome:", ocorrencia["nome"])

    registrar_acao(f"Atendimento da ocorrência {ocorrencia['id']}")


def mostrar_historico():
    print("\nHISTÓRICO")

    if not historico:
        print("Nenhuma ação registrada.")
        return

    for acao in reversed(historico):
        print(acao)

def ordenar_por_prioridade():
    print("\nOCORRÊNCIAS ORDENADAS POR PRIORIDADE")

    if not ocorrencias:
        print("Nenhuma ocorrência cadastrada.")
        return

    lista_ordenada = ocorrencias.copy()

    n = len(lista_ordenada)

    for i in range(n):
        indice_maior = i

        for j in range(i + 1, n):
            if lista_ordenada[j]["prioridade"] > lista_ordenada[indice_maior]["prioridade"]:
                indice_maior = j

        lista_ordenada[i], lista_ordenada[indice_maior] = (
            lista_ordenada[indice_maior],
            lista_ordenada[i]
        )

    for oc in lista_ordenada:
        print("---------------------")
        print("ID:", oc["id"])
        print("Nome:", oc["nome"])
        print("Tipo:", oc["tipo"])
        print("Descrição:", oc["descricao"])
        print("Prioridade:", oc["prioridade"])

    registrar_acao("Ordenação por prioridade usando Selection Sort")

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar ocorrências")
    print("3 - Buscar por ID")
    print("4 - Buscar por nome")
    print("5 - Buscar por tipo")
    print("6 - Atender próxima ocorrência")
    print("7 - Mostrar histórico")
    print("8 - Ordenar por prioridade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()

    elif opcao == "2":
        listar_ocorrencias()

    elif opcao == "3":
        buscar_por_id()

    elif opcao == "4":
        buscar_por_nome()

    elif opcao == "5":
        buscar_por_tipo()

    elif opcao == "6":
        atender_proxima_ocorrencia()

    elif opcao == "7":
        mostrar_historico()
        
    elif opcao == "8":
        ordenar_por_prioridade()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")