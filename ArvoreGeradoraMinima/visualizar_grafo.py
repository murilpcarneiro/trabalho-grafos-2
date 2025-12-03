"""
Script para gerar uma visualização gráfica da Árvore Geradora Mínima.
Requer: pip install matplotlib networkx
"""

try:
    import matplotlib.pyplot as plt
    import networkx as nx
    from mst_cidades import criar_mapa_brasil_ponderado
except ImportError:
    print("[ERRO] Instale as bibliotecas necessárias:")
    print("   pip install matplotlib networkx")
    exit(1)


def desenhar_mst(algoritmo="kruskal"):
    """Desenha a Árvore Geradora Mínima como um grafo visual."""
    print(f"Gerando visualização da MST usando {algoritmo.upper()}...")

    grafo = criar_mapa_brasil_ponderado()

    if algoritmo.lower() == "kruskal":
        resultado = grafo.kruskal()
    else:
        resultado = grafo.prim()

    if not resultado:
        print("[ERRO] Falha ao calcular MST")
        return None

    arestas_mst, peso_total = resultado

    G_completo = nx.Graph()
    for aresta in grafo.arestas:
        G_completo.add_edge(aresta.origem, aresta.destino, weight=aresta.peso)

    G_mst = nx.Graph()
    for aresta in arestas_mst:
        G_mst.add_edge(aresta.origem, aresta.destino, weight=aresta.peso)

    plt.figure(figsize=(16, 12))

    pos = nx.spring_layout(G_completo, k=3, iterations=50, seed=42)

    arestas_nao_usadas = [e for e in G_completo.edges()
                          if not G_mst.has_edge(e[0], e[1])]
    nx.draw_networkx_edges(G_completo, pos, edgelist=arestas_nao_usadas,
                           alpha=0.2, width=1, edge_color='lightgray', style='dashed')

    nx.draw_networkx_edges(G_mst, pos, edgelist=G_mst.edges(),
                           edge_color='red', width=3, alpha=0.8)

    nx.draw_networkx_nodes(G_completo, pos, node_color='lightblue',
                           node_size=800, alpha=0.9)

    nx.draw_networkx_labels(G_completo, pos, font_size=9, font_weight='bold')

    edge_labels = {(u, v): f"{d['weight']:.0f}"
                   for u, v, d in G_mst.edges(data=True)}
    nx.draw_networkx_edge_labels(G_mst, pos, edge_labels, font_size=8)

    economia_pct = ((sum(a.peso for a in grafo.arestas) - peso_total) /
                    sum(a.peso for a in grafo.arestas)) * 100

    plt.title(f"Árvore Geradora Mínima ({algoritmo.upper()})\n"
              f"Arestas: {len(arestas_mst)} | Distância: {peso_total:.0f} km | "
              f"Economia: {economia_pct:.1f}%",
              fontsize=14, fontweight='bold')

    from matplotlib.lines import Line2D
    legenda_elements = [
        Line2D([0], [0], color='red', lw=3, label='Arestas na MST'),
        Line2D([0], [0], color='lightgray', lw=1, linestyle='--', label='Arestas não usadas')
    ]
    plt.legend(handles=legenda_elements, loc='upper left', fontsize=11)

    plt.axis('off')
    plt.tight_layout()

    return plt


def exemplo_visualizacao():
    """Demonstra as visualizações possíveis."""
    print("\n" + "="*70)
    print("VISUALIZADOR DE GRAFOS - MST (Árvore Geradora Mínima)")
    print("="*70)
    print("\nOpções de visualização:")
    print("1. MST usando Kruskal")
    print("2. MST usando Prim")
    print("3. Comparar lado a lado (2 imagens)")
    print("="*70)

    opcao = input("\nEscolha uma opção (1-3): ").strip()

    if opcao == "1":
        plt = desenhar_mst("kruskal")
        if plt:
            arquivo = "mst_kruskal.png"
            plt.savefig(arquivo, dpi=300, bbox_inches='tight')
            print(f"\n[OK] Imagem salva como: {arquivo}")
            print("[OK] Abrindo visualização...")
            plt.show()

    elif opcao == "2":
        plt = desenhar_mst("prim")
        if plt:
            arquivo = "mst_prim.png"
            plt.savefig(arquivo, dpi=300, bbox_inches='tight')
            print(f"\n[OK] Imagem salva como: {arquivo}")
            print("[OK] Abrindo visualização...")
            plt.show()

    elif opcao == "3":
        print("\nGerando ambas as visualizações...")

        plt1 = desenhar_mst("kruskal")
        if plt1:
            arquivo1 = "mst_kruskal.png"
            plt1.savefig(arquivo1, dpi=300, bbox_inches='tight')
            print(f"[OK] Imagem 1 salva como: {arquivo1}")
            plt1.close()

        plt2 = desenhar_mst("prim")
        if plt2:
            arquivo2 = "mst_prim.png"
            plt2.savefig(arquivo2, dpi=300, bbox_inches='tight')
            print(f"[OK] Imagem 2 salva como: {arquivo2}")
            plt2.show()

    else:
        print("[ERRO] Opção inválida!")
        return


if __name__ == "__main__":
    exemplo_visualizacao()
