"""
Sistema de Gerenciamento de Produtos
Desenvolvido para demonstrar o uso de Listas, Tuplas, Conjuntos e
a equivalência lógica em Portugal.
"""

def executar_sistema():
    print("=== SISTEMA DE GESTÃO DE PRODUTOS ==-\n")
    
    # ----------------------------------------------------
    # 1. Cadastro de Produtos
    # ----------------------------------------------------
    # Em Python, usamos uma lista para armazenar dicionários com os dados.
    # 
    # [PORTUGAL - Equivalente comentado]:
    # Algoritmo CadastroProdutos
    # Var
    #   nomes: vetor[1..100] de caractere
    #   precos: vetor[1..100] de real
    #   categorias: vetor[1..100] de caractere
    #   i, qtd: inteiro
    # Inicio
    #   escreval("Quantos produtos deseja cadastrar?")
    #   leia(qtd)
    #   para i de 1 ate qtd faca
    #     escreval("Nome: ")
    #     leia(nomes[i])
    #     escreval("Preço: ")
    #     leia(precos[i])
    #     escreval("Categoria: ")
    #     leia(categorias[i])
    #   fimpara
    # FimAlgoritmo
    
    produtos = []
    
    # Para testes práticos, podemos cadastrar alguns produtos de exemplo 
    # ou usar um laço com input(). Vamos simular um cadastro flexível:
    print("Cadastre seus produtos (digite 'fim' no nome para encerrar):")
    while True:
        nome_produto = input("Nome do produto: ").strip()
        if nome_produto.lower() == 'fim':
            break
            
        try:
            preco_produto = float(input("Preço do produto (R$): "))
            if preco_produto <= 0:
                print("O preço deve ser maior que zero.")
                continue
        except ValueError:
            print("Valor inválido para o preço. Digite um número.")
            continue
            
        categoria_produto = input("Categoria do produto: ").strip()
        
        # Armazenando na lista usando append
        produtos.append({
            "nome": nome_produto,
            "preco": preco_produto,
            "categoria": categoria_produto
        })
        print("Produto cadastrado com sucesso!\n")

    if not produtos:
        print("Nenhum produto foi cadastrado.")
        return

    # ----------------------------------------------------
    # 2. Filtragem por Preço
    # ----------------------------------------------------
    print("\n--- FILTRAGEM POR PREÇO ---")
    try:
        limite_preco = float(input("Informe um valor de referência para filtrar: R$ "))
        opcao_filtro = input("Deseja produtos [A]cima ou [B]baixo desse valor? ").strip().upper()
        
        if opcao_filtro == 'A':
            produtos_filtrados = [p for p in produtos if p["preco"] > limite_preco]
            print(f"\nProdutos acima de R$ {limite_preco:.2f}:")
        else:
            produtos_filtrados = [p for p in produtos if p["preco"] < limite_preco]
            print(f"\nProdutos abaixo de R$ {limite_preco:.2f}:")
            
        for p in produtos_filtrados:
            print(f"- {p['nome']} (R$ {p['preco']:.2f})")
    except ValueError:
        print("Valor de filtro inválido.")

    # ----------------------------------------------------
    # 3. Ordenação
    # ----------------------------------------------------
    # sort() modifica a lista original (crescente)
    # sorted() cria uma nova lista (decrescente)
    #
    # [PORTUGAL - Equivalente Bubble Sort para Ordenação]:
    # para i de 1 ate qtd-1 faca
    #   para j de 1 ate qtd-i faca
    #     se precos[j] > precos[j+1] entao
    #       aux = precos[j]; precos[j] = precos[j+1]; precos[j+1] = aux
    #     fimse
    #   fimpara
    # fimpara
    
    # Criamos cópias para preservar a lista original se necessário
    produtos_crescente = sorted(produtos, key=lambda x: x["preco"])
    produtos_decrescente = sorted(produtos, key=lambda x: x["preco"], reverse=True)

    print("\n--- ORDENAÇÃO DE PREÇOS ---")
    print("Preços Crescentes:")
    for p in produtos_crescente:
        print(f"  {p['nome']} - R$ {p['preco']:.2f}")

    print("\nPreços Decrescentes:")
    for p in produtos_decrescente:
        print(f"  {p['nome']} - R$ {p['preco']:.2f}")

    # ----------------------------------------------------
    # 4. Conjunto de Categorias Únicas (set)
    # ----------------------------------------------------
    # O set() elimina duplicatas automaticamente de forma eficiente.
    #
    # [PORTUGAL - Simulação manual de Conjunto]:
    # Percorrer o vetor de categorias comparando com uma lista de únicos:
    # duplicado <- falso
    # para i de 1 ate qtd faca
    #   para j de 1 ate k faca
    #     se categorias[i] == categorias_unicas[j] entao duplicado <- verdadeiro
    #   fimpara
    #   se nao duplicado entao categorias_unicas[k++] <- categorias[i]
    # fimpara
    
    categorias_unicas = {p["categoria"] for p in produtos}

    # ----------------------------------------------------
    # 5. Tupla de Estatísticas
    # ----------------------------------------------------
    # Tupla imutável para agrupar dados consolidados (menor, maior, média)
    precos_lista = [p["preco"] for p in produtos]
    menor_preco = min(precos_lista)
    maior_preco = max(precos_lista)
    media_preco = sum(precos_lista) / len(precos_lista)
    
    estatisticas = (menor_preco, maior_preco, media_preco)

    # ----------------------------------------------------
    # 6. Relatório Final Formatado (f-strings)
    # ----------------------------------------------------
    print("\n" + "="*40)
    print("          RELATÓRIO FINAL DO SISTEMA")
    print("="*40)
    print(f"Total de produtos cadastrados: {len(produtos)}")
    print(f"Categorias cadastradas (Únicas): {', '.join(categorias_unicas)}")
    print("-" * 40)
    print("ESTATÍSTICAS DE PREÇOS:")
    print(f"  • Menor Preço: R$ {estatisticas[0]:.2f}")
    print(f"  • Maior Preço: R$ {estatisticas[1]:.2f}")
    print(f"  • Preço Médio: R$ {estatisticas[2]:.2f}")
    print("="*40)

if __name__ == "__main__":
    executar_sistema()
    