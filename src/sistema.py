# ==============================================================================
# NEIGHBORHOOD ACTION DASHBOARD - GLOBAL SOLUTION (GRUPO 46)
# Aluno: Pedro Fattorelli Carrion
# ==============================================================================

# Estruturas de Dados Principais
lista_ocorrencias = []
dicionario_ocorrencias = {}
fila_novas_demandas = []
pilha_historico = []

# Parâmetros e Domínios Válidos
CATEGORIAS_VALIDAS = ["iluminação", "acessibilidade", "limpeza", "conservação"]
SITUACOES_VALIDAS = ["aberta", "em análise", "concluída"]


def inicializar_dados_iniciais():
    """Carrega as 12 ocorrências iniciais obrigatórias (com 1 registro inconsistente para teste)."""
    dados_iniciais = [
        {"id": "001", "categoria": "iluminação", "descricao": "Poste apagado na via pública", "local": "Praça Central", "data": "01/11/2026", "status": "aberta"},
        {"id": "002", "categoria": "acessibilidade", "descricao": "Calçada com buraco e sem rampa", "local": "Rua das Flores, 120", "data": "02/11/2026", "status": "em análise"},
        {"id": "003", "categoria": "limpeza", "descricao": "Acúmulo de entulho e lixo na esquina", "local": "Avenida Brasil", "data": "03/11/2026", "status": "aberta"},
        {"id": "004", "categoria": "conservação", "descricao": "Banco da praça quebrado", "local": "Praça da Matriz", "data": "04/11/2026", "status": "concluída"},
        {"id": "005", "categoria": "iluminação", "descricao": "Fiação exposta em poste de luz", "local": "Rua Principal", "data": "05/11/2026", "status": "aberta"},
        {"id": "006", "categoria": "acessibilidade", "descricao": "Falta de piso tátil na travessia", "local": "Esquina Rua A", "data": "06/11/2026", "status": "aberta"},
        {"id": "007", "categoria": "limpeza", "descricao": "Bueiro entupido gerando alagamento", "local": "Rua B", "data": "07/11/2026", "status": "em análise"},
        {"id": "008", "categoria": "conservação", "descricao": "Pintura de sinalização de trânsito apagada", "local": "Avenida Central", "data": "08/11/2026", "status": "concluída"},
        {"id": "009", "categoria": "iluminação", "descricao": "Galho de árvore obstruindo a iluminação", "local": "Rua das Palmeiras", "data": "09/11/2026", "status": "aberta"},
        {"id": "010", "categoria": "acessibilidade", "descricao": "Sinal sonoro de semáforo quebrado", "local": "Cruzamento Principal", "data": "10/11/2026", "status": "concluída"},
        {"id": "011", "categoria": "limpeza", "descricao": "Descarte irregular de móveis velhos", "local": "Rua dos Limoeiros", "data": "11/11/2026", "status": "aberta"},
        # Registro inconsistente proposital para testar a validação
        {"id": "012", "categoria": "invalida", "descricao": "Registro com dados incorretos de teste", "local": "Desconhecido", "data": "12/11/2026", "status": "pendente"}
    ]

    for item in dados_iniciais:
        lista_ocorrencias.append(item)
        dicionario_ocorrencias[item["id"]] = item
        if item["status"] == "aberta":
            fila_novas_demandas.append(item["id"])
            
    # Histórico simulado inicial (8 eventos na pilha LIFO)
    historico_inicial = [
        "Ocorrência 012 cadastrada com inconsistência de dados",
        "Ocorrência 011 registrada na fila de triagem",
        "Ocorrência 010 marcada como concluída",
        "Ocorrência 009 registrada na fila de triagem",
        "Ocorrência 008 alterada para concluída",
        "Ocorrência 007 movida para em análise",
        "Ocorrência 002 alterada para em análise",
        "Sistema inicializado com sucesso"
    ]
    for evento in historico_inicial:
        pilha_historico.append(evento)


def validar_ocorrencia(cat, stat):
    """Regra lógica utilizando operadores AND, OR e NOT."""
    if not cat or not stat:
        return False
    if (cat not in CATEGORIAS_VALIDAS) or (stat not in SITUACOES_VALIDAS):
        return False
    return True


def cadastrar_ocorrencia():
    print("\n--- CADASTRAR NOVA OCORRÊNCIA ---")
    novo_id = input("Digite o código identificador único (ex: 013): ").strip()
    
    if novo_id in dicionario_ocorrencias:
        print("Erro: Já existe uma ocorrência cadastrada com este código!")
        return

    print(f"Categorias válidas: {CATEGORIAS_VALIDAS}")
    categoria = input("Digite a categoria: ").strip().lower()
    descricao = input("Digite a descrição breve: ").strip()
    local = input("Digite a localidade genérica: ").strip()
    data = input("Digite a data simulada (DD/MM/AAAA): ").strip()
    print(f"Situações válidas: {SITUACOES_VALIDAS}")
    status = input("Digite a situação atual: ").strip().lower()

    if not validar_ocorrencia(categoria, status) or not descricao or not local:
        print("Erro de validação: Campos obrigatórios vazios ou categoria/status inválidos!")
        pilha_historico.append(f"Tentativa de cadastro falhou para o ID {novo_id} devido a dados inválidos")
        return

    nova_oc = {
        "id": novo_id,
        "categoria": categoria,
        "descricao": descricao,
        "local": local,
        "data": data,
        "status": status
    }

    lista_ocorrencias.append(nova_oc)
    dicionario_ocorrencias[novo_id] = nova_oc
    
    if status == "aberta":
        fila_novas_demandas.append(novo_id)

    pilha_historico.append(f"Nova ocorrência cadastrada com sucesso: ID {novo_id}")
    print("Ocorrência cadastrada com sucesso!")


def listar_ocorrencias():
    print("\n--- LISTAGEM GERAL DE OCORRÊNCIAS ---")
    if not lista_ocorrencias:
        print("Nenhuma ocorrência registrada.")
        return

    print(f"{'ID':<5} | {'CATEGORIA':<15} | {'LOCALIDADE':<20} | {'STATUS':<12} | {'DESCRIÇÃO'}")
    print("-" * 75)
    for oc in lista_ocorrencias:
        print(f"{oc['id']:<5} | {oc['categoria']:<15} | {oc['local']:<20} | {oc['status']:<12} | {oc['descricao']}")


def consultar_por_filtros():
    print("\n--- CONSULTAR E FILTRAR OCORRÊNCIAS ---")
    print("1. Consultar por ID específico")
    print("2. Filtrar por Categoria")
    print("3. Filtrar por Status")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        codigo = input("Digite o código ID: ").strip()
        if codigo in dicionario_ocorrencias:
            oc = dicionario_ocorrencias[codigo]
            print(f"\n[ENCONTRADO] ID: {oc['id']} | Categoria: {oc['categoria']} | Local: {oc['local']} | Status: {oc['status']}")
            print(f"Descrição: {oc['descricao']} | Data: {oc['data']}")
        else:
            print("Ocorrência não encontrada.")
            
    elif opcao == "2":
        cat = input(f"Digite a categoria desejada {CATEGORIAS_VALIDAS}: ").strip().lower()
        encontrados = [oc for oc in lista_ocorrencias if oc['categoria'] == cat]
        if encontrados:
            print(f"\n--- Ocorrências da Categoria: {cat} ---")
            for oc in encontrados:
                print(f"ID: {oc['id']} | Local: {oc['local']} | Status: {oc['status']} | Descrição: {oc['descricao']}")
        else:
            print("Nenhuma ocorrência encontrada para esta categoria.")
            
    elif opcao == "3":
        stat = input(f"Digite o status desejado {SITUACOES_VALIDAS}: ").strip().lower()
        encontrados = [oc for oc in lista_ocorrencias if oc['status'] == stat]
        if encontrados:
            print(f"\n--- Ocorrências com Status: {stat} ---")
            for oc in encontrados:
                print(f"ID: {oc['id']} | Categoria: {oc['categoria']} | Local: {oc['local']} | Descrição: {oc['descricao']}")
        else:
            print("Nenhuma ocorrência encontrada para este status.")
    else:
        print("Opção inválida.")


def atualizar_status():
    print("\n--- ATUALIZAR STATUS DE OCORRÊNCIA ---")
    codigo = input("Digite o ID da ocorrência que deseja atualizar: ").strip()

    if codigo not in dicionario_ocorrencias:
        print("Erro: Ocorrência não encontrada com esse ID.")
        return

    oc = dicionario_ocorrencias[codigo]
    print(f"Ocorrência atual: ID {oc['id']} | Status atual: {oc['status']} | Descrição: {oc['descricao']}")
    
    novo_status = input(f"Digite o novo status {SITUACOES_VALIDAS}: ").strip().lower()

    if not novo_status or (novo_status not in SITUACOES_VALIDAS):
        print("Erro: Situação inválida ou vazia informada!")
        return

    status_antigo = oc["status"]
    oc["status"] = novo_status
    
    if status_antigo == "aberta" and novo_status != "aberta":
        if codigo in fila_novas_demandas:
            fila_novas_demandas.remove(codigo)

    pilha_historico.append(f"Ocorrência {codigo} alterada de '{status_antigo}' para '{novo_status}'")
    print("Status atualizado com sucesso!")


def exibir_indicadores():
    print("\n--- PAINEL DE INDICADORES DA COMUNIDADE ---")
    total = len(lista_ocorrencias)
    if total == 0:
        print("Sem dados suficientes para indicadores.")
        return

    qtd_aberta = sum(1 for oc in lista_ocorrencias if oc["status"] == "aberta")
    qtd_analise = sum(1 for oc in lista_ocorrencias if oc["status"] == "em análise")
    qtd_concluida = sum(1 for oc in lista_ocorrencias if oc["status"] == "concluída")

    print(f"Total de ocorrências cadastradas: {total}")
    print(f"- Abertas: {qtd_aberta} ({ (qtd_aberta/total)*100:.1f}%)")
    print(f"- Em Análise: {qtd_analise} ({ (qtd_analise/total)*100:.1f}%)")
    print(f"- Concluídas: {qtd_concluida} ({ (qtd_concluida/total)*100:.1f}%)")

    print("\n--- MATRIZ RESUMO (CATEGORIA x SITUAÇÃO) ---")
    print(f"{'CATEGORIA':<15} | {'ABERTA':<8} | {'EM ANÁLISE':<10} | {'CONCLUÍDA'}")
    print("-" * 55)
    
    for cat in CATEGORIAS_VALIDAS:
        ab = sum(1 for oc in lista_ocorrencias if oc["categoria"] == cat and oc["status"] == "aberta")
        an = sum(1 for oc in lista_ocorrencias if oc["categoria"] == cat and oc["status"] == "em análise")
        co = sum(1 for oc in lista_ocorrencias if oc["categoria"] == cat and oc["status"] == "concluída")
        print(f"{cat:<15} | {ab:<8} | {an:<10} | {co}")

    print(f"\nDemandas pendentes na Fila de Triagem (FIFO): {len(fila_novas_demandas)}")
    print(f"Eventos registrados na Pilha de Histórico (LIFO): {len(pilha_historico)}")
    if pilha_historico:
        print(f"Última movimentação registrada: {pilha_historico[-1]}")


def main():
    inicializar_dados_iniciais()
    while True:
        print("\n=============================================")
        print("   NEIGHBORHOOD ACTION DASHBOARD - GRUPO 46  ")
        print("=============================================")
        print("1. Listar todas as ocorrências")
        print("2. Cadastrar nova ocorrência")
        print("3. Consultar / Filtrar ocorrências")
        print("4. Atualizar status de uma ocorrência")
        print("5. Exibir painel de indicadores")
        print("6. Sair do sistema")
        
        opcao = input("Escolha uma opção (1-6): ").strip()
        
        if opcao == "1":
            listar_ocorrencias()
        elif opcao == "2":
            cadastrar_ocorrencia()
        elif opcao == "3":
            consultar_por_filtros()
        elif opcao == "4":
            atualizar_status()
        elif opcao == "5":
            exibir_indicadores()
        elif opcao == "6":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 6.")


if __name__ == "__main__":
    main()
