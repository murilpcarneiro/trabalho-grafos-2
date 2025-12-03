# Script para visualizar graficamente o mapa de cidades usando matplotlib e networkx

try:
    import matplotlib.pyplot as plt
    import networkx as nx
    from bfs_cidades import criar_mapa_brasil
except ImportError:
    print("❌ ERRO: Instale as bibliotecas necessárias:")
    print("   pip install matplotlib networkx")
    exit(1)


def desenhar_mapa(destacar_caminho=None):
    # Desenha o mapa de cidades como grafo visual, opcionalmente destacando um caminho
    print("Gerando visualização do mapa...")

    # Cria o mapa
    mapa_obj = criar_mapa_brasil()

    # Converte para NetworkX
    G = nx.Graph()
    for cidade, vizinhos in mapa_obj.grafo.items():
        for vizinho in vizinhos:
            G.add_edge(cidade, vizinho)

    # Configurações de layout
    plt.figure(figsize=(16, 12))

    # Layout - posição dos nós
    # Usando spring layout para distribuição automática
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Desenha as arestas (estradas)
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=2, edge_color='gray')

    # Se há um caminho para destacar
    if destacar_caminho and len(destacar_caminho) > 1:
        # Cria lista de arestas do caminho
        caminho_edges = [(destacar_caminho[i], destacar_caminho[i+1])
                         for i in range(len(destacar_caminho)-1)]

        # Desenha o caminho destacado
        nx.draw_networkx_edges(G, pos, edgelist=caminho_edges,
                               edge_color='red', width=4, alpha=0.8)

        # Destaca os nós do caminho
        nx.draw_networkx_nodes(G, pos, nodelist=destacar_caminho,
                               node_color='red', node_size=800, alpha=0.9)

        # Destaca origem e destino
        nx.draw_networkx_nodes(G, pos, nodelist=[destacar_caminho[0]],
                               node_color='green', node_size=1000, alpha=1)
        nx.draw_networkx_nodes(G, pos, nodelist=[destacar_caminho[-1]],
                               node_color='blue', node_size=1000, alpha=1)

        # Outros nós
        outros_nos = [n for n in G.nodes() if n not in destacar_caminho]
        nx.draw_networkx_nodes(G, pos, nodelist=outros_nos,
                               node_color='lightblue', node_size=600, alpha=0.7)
    else:
        # Desenha todos os nós normalmente
        nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                               node_size=600, alpha=0.7)

    # Adiciona os nomes das cidades
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

    # Título e configurações
    if destacar_caminho:
        plt.title(f"Mapa de Cidades - Caminho: {destacar_caminho[0]} → {destacar_caminho[-1]}\n"
                  f"Distância: {len(destacar_caminho)-1} conexões",
                  fontsize=16, fontweight='bold')
    else:
        plt.title("Mapa Completo de Cidades Brasileiras\n"
                  "20 Cidades, 28 Conexões",
                  fontsize=16, fontweight='bold')

    plt.axis('off')
    plt.tight_layout()

    return plt


def exemplo_visualizacao():
    # Demonstra as visualizações possíveis com opção de salvar e exibir
    print("\n" + "="*70)
    print("VISUALIZADOR DE GRAFOS - BFS")
    print("="*70)
    print("\nOpções de visualização:")
    print("1. Mapa completo (sem caminho destacado)")
    print("2. Exemplo: São Paulo → Fortaleza")
    print("3. Exemplo: Manaus → Porto Alegre")
    print("4. Exemplo: Rio de Janeiro → Cuiabá")
    print("="*70)

    opcao = input("\nEscolha uma opção (1-4): ").strip()

    if opcao == "1":
        plt = desenhar_mapa()
        arquivo = "mapa_completo.png"
    elif opcao == "2":
        mapa = criar_mapa_brasil()
        resultado = mapa.bfs_caminho_mais_curto("São Paulo", "Fortaleza")
        if resultado:
            caminho, _ = resultado
            plt = desenhar_mapa(destacar_caminho=caminho)
            arquivo = "caminho_sp_fortaleza.png"
    elif opcao == "3":
        mapa = criar_mapa_brasil()
        resultado = mapa.bfs_caminho_mais_curto("Manaus", "Porto Alegre")
        if resultado:
            caminho, _ = resultado
            plt = desenhar_mapa(destacar_caminho=caminho)
            arquivo = "caminho_manaus_poa.png"
    elif opcao == "4":
        mapa = criar_mapa_brasil()
        resultado = mapa.bfs_caminho_mais_curto("Rio de Janeiro", "Cuiabá")
        if resultado:
            caminho, _ = resultado
            plt = desenhar_mapa(destacar_caminho=caminho)
            arquivo = "caminho_rio_cuiaba.png"
    else:
        print("Opção inválida!")
        return

    # Salva a imagem
    plt.savefig(arquivo, dpi=300, bbox_inches='tight')
    print(f"\n✓ Imagem salva como: {arquivo}")

    # Mostra na tela
    print("✓ Abrindo visualização...")
    plt.show()


if __name__ == "__main__":
    # Executa o visualizador (requer: pip install matplotlib networkx)
    exemplo_visualizacao()
