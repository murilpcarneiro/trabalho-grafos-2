import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

class GrafoCidadesBrasil:
    def __init__(self, num_vertices):
        # numero cidades no grafo
        self.V = num_vertices 
        # Lista de arestas: origem, destino, distancia 
        self.arestas = []
        # Mapa de índices para nomes de cidades
        self.cidades = {}
        # Grafo para visualização
        self.G = nx.DiGraph()

    # Adiciona uma cidade ao mapa
    def adicionar_cidade(self, indice, nome):
        self.cidades[indice] = nome
        self.G.add_node(indice, label=nome)

    # Adiciona uma aresta (rota entre duas cidades com distância em km)
    def adicionar_aresta(self, u, v, distancia_km):
        self.arestas.append((u, v, distancia_km))
        self.G.add_edge(u, v, weight=distancia_km)

    # Implementação do Algoritmo Bellman-Ford
    def bellman_ford(self, origem):
        """
        Calcula as distâncias mais curtas da origem até todas as cidades
        usando Bellman-Ford e detecta ciclos negativos.
        """
        # 1. Inicialização
        distancias = {v: float('inf') for v in range(self.V)}
        distancias[origem] = 0

        # Array para reconstruir o caminho 
        predecessores = {v: None for v in range(self.V)}
        
        # 2. Loop Principal
        print(f"\n--- Relaxamento de Arestas (Iterações 1 a {self.V - 1}) ---")
        for i in range(self.V - 1):
            mudanca = False
            # Percorre as arestas
            for u, v, w in self.arestas:
                # Se a distância de 'u' for finita E o novo caminho via 'u' for mais curto
                if distancias[u] != float('inf') and distancias[u] + w < distancias[v]:
                    # Operação de Relaxamento
                    distancias[v] = distancias[u] + w
                    predecessores[v] = u
                    mudanca = True
            
            # Otimização: Se nenhuma distância foi atualizada, convergiu
            if not mudanca:
                print(f"  ✓ Convergência alcançada na iteração {i + 1}")
                break
            else:
                print(f"  - Iteração {i + 1} concluída (arestas relaxadas)")
        
        # 3. Detecção de Ciclo de Peso Negativo
        print("\n--- Verificação de Ciclos Negativos ---")
        for u, v, w in self.arestas:
            if distancias[u] != float('inf') and distancias[u] + w < distancias[v]:
                return (False, "ERRO: Ciclo negativo detectado!", distancias, predecessores)
        
        print("  ✓ Nenhum ciclo negativo encontrado")
        return (True, "Sucesso! Caminhos mais curtos calculados.", distancias, predecessores)
    
    def visualizar_grafo(self, predecessores, origem, destino=None):
        """Visualiza o grafo com o caminho mais curto destacado"""
        plt.figure(figsize=(16, 10))
        
        # Layout do grafo
        pos = nx.spring_layout(self.G, k=2, iterations=50, seed=42)
        
        # Desenha todas as arestas em cinza
        nx.draw_networkx_edges(self.G, pos, edge_color='lightgray', 
                              arrows=True, arrowsize=20, width=1.5,
                              connectionstyle="arc3,rad=0.1", alpha=0.6)
        
        # Destaca o caminho se um destino foi especificado
        if destino is not None:
            caminho_arestas = []
            atual = destino
            while atual is not None and predecessores[atual] is not None:
                caminho_arestas.append((predecessores[atual], atual))
                atual = predecessores[atual]
            
            # Desenha o caminho destacado em vermelho
            nx.draw_networkx_edges(self.G, pos, edgelist=caminho_arestas, 
                                  edge_color='red', width=3, arrows=True, 
                                  arrowsize=25, connectionstyle="arc3,rad=0.1")
        
        # Cores dos nós
        node_colors = []
        for node in self.G.nodes():
            if node == origem:
                node_colors.append('#90EE90')  
            elif destino is not None and node == destino:
                node_colors.append('#FF6B6B')  
            else:
                node_colors.append('#87CEEB')  
        
        # Desenha os nós
        nx.draw_networkx_nodes(self.G, pos, node_color=node_colors, 
                              node_size=2000, alpha=0.9)
        
        # Desenha os rótulos das cidades
        labels = {node: self.cidades[node] for node in self.G.nodes()}
        nx.draw_networkx_labels(self.G, pos, labels, font_size=8, 
                               font_weight='bold')
        
        # Desenha os pesos das arestas 
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        edge_labels = {k: f"{v:.0f}km" for k, v in edge_labels.items()}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels, font_size=7)
        
        legenda_info = f"Origem: {self.cidades[origem]} (🟢)\n"
        if destino is not None:
            legenda_info += f"Destino: {self.cidades[destino]} (🔴)\n"
            legenda_info += "Caminho mais curto (vermelho)"
        
        plt.title("Caminho Mais Curto Entre Cidades do Brasil\nAlgoritmo: Bellman-Ford", 
                 fontsize=14, fontweight='bold')
        plt.text(0.02, 0.98, legenda_info, transform=plt.gca().transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
def reconstruir_caminho(predecessores, cidades, origem, destino):
    """Reconstrói o caminho da origem ao destino"""
    caminho = []
    atual = destino
    
    while atual is not None:
        caminho.append(atual)
        if atual == origem:
            break
        atual = predecessores.get(atual)
    
    # Verifica se o nó é alcançável
    if caminho[-1] != origem:
        return "Caminho inacessível"
    
    # Converte índices para nomes de cidades
    caminho_nomes = [cidades.get(c, f"Cidade {c}") for c in reversed(caminho)]
    return " → ".join(caminho_nomes)

def exibir_menu_cidades(cidades):
    """Exibe menu de seleção de cidades"""
    print(f"\n{'='*60}")
    print("LISTA DE CIDADES DISPONÍVEIS")
    print(f"{'='*60}\n")
    
    for idx, cidade in cidades.items():
        print(f"  [{idx:2d}] {cidade}")
    
    print()

def selecionar_cidade(cidades, tipo="origem"):
    """Permite ao usuário selecionar uma cidade"""
    while True:
        try:
            exibir_menu_cidades(cidades)
            entrada = input(f"Digite o número da cidade de {tipo}: ").strip()
            
            indice = int(entrada)
            
            if indice not in cidades:
                print(f"❌ Erro: Índice {indice} não encontrado. Tente novamente.")
                continue
            
            print(f"✓ Cidade selecionada: {cidades[indice]}")
            return indice
            
        except ValueError:
            print("❌ Erro: Digite um número válido.")

# Exemplo de execução
if __name__ == "__main__":
    # Criando grafo com 16 cidades brasileiras
    N = 16
    g = GrafoCidadesBrasil(N)

    # 1. Adicionando as cidades
    cidades_lista = [
        "São Paulo", "Rio de Janeiro", "Brasília", "Salvador",
        "Fortaleza", "Belo Horizonte", "Manaus", "Curitiba",
        "Recife", "Porto Alegre", "Goiânia", "Belém",
        "Campinas", "Sorocaba", "Santos", "Ribeirão Preto"
    ]
    
    for i, cidade in enumerate(cidades_lista):
        g.adicionar_cidade(i, cidade)

    # 2. Adicionando arestas
    g.adicionar_aresta(0, 1, 430)    # São Paulo → Rio de Janeiro
    g.adicionar_aresta(0, 5, 586)    # São Paulo → Belo Horizonte
    g.adicionar_aresta(1, 3, 1621)   # Rio de Janeiro → Salvador
    g.adicionar_aresta(1, 5, 525)    # Rio de Janeiro → Belo Horizonte
    g.adicionar_aresta(2, 10, 209)   # Brasília → Goiânia
    g.adicionar_aresta(3, 8, 839)    # Salvador → Recife
    g.adicionar_aresta(4, 8, 588)    # Fortaleza → Recife
    g.adicionar_aresta(5, 2, 716)    # Belo Horizonte → Brasília
    g.adicionar_aresta(5, 0, 586)    # Belo Horizonte → São Paulo
    g.adicionar_aresta(6, 11, 1658)  # Manaus → Belém
    g.adicionar_aresta(7, 9, 1210)   # Curitiba → Porto Alegre
    g.adicionar_aresta(10, 3, 1474)  # Goiânia → Salvador
    g.adicionar_aresta(11, 6, 1658)  # Belém → Manaus
    g.adicionar_aresta(12, 0, 99)    # Campinas → São Paulo
    g.adicionar_aresta(13, 0, 108)   # Sorocaba → São Paulo
    g.adicionar_aresta(14, 0, 71)    # Santos → São Paulo
    g.adicionar_aresta(15, 0, 308)   # Ribeirão Preto → São Paulo
    g.adicionar_aresta(0, 7, 408)    # São Paulo → Curitiba
    g.adicionar_aresta(5, 10, 507)   # Belo Horizonte → Goiânia

    # 3. Menu de seleção
    print(f"\n{'='*60}")
    print("CAMINHO MAIS CURTO ENTRE CIDADES DO BRASIL")
    print(f"Algoritmo: Bellman-Ford")
    print(f"{'='*60}")
    
    # Selecionar origem
    origem = selecionar_cidade(g.cidades, "origem")
    
    # Selecionar destino
    destino = selecionar_cidade(g.cidades, "destino")
    
    # Validar se origem e destino são diferentes
    if origem == destino:
        print("\n❌ Erro: A origem e o destino devem ser cidades diferentes!")
        exit()
    
    # 4. Execução do Bellman-Ford
    print(f"\n{'='*60}")
    print(f"ALGORITMO BELLMAN-FORD: CAMINHO MAIS CURTO ENTRE CIDADES")
    print(f"{'='*60}")
    print(f"\nOrigem: {g.cidades[origem]}")
    
    sucesso, mensagem, distancias, predecessores = g.bellman_ford(origem)

    # 5. Impressão dos Resultados
    print(f"\n{'='*60}")
    print("RESULTADO FINAL")
    print(f"{'='*60}")
    print(f"\n{mensagem}\n")
    
    if sucesso:
        print(f"Distâncias mínimas a partir de {g.cidades[origem]}:\n")
        for v in range(N):
            caminho = reconstruir_caminho(predecessores, g.cidades, origem, v)
            dist = distancias[v]
            if dist == float('inf'):
                dist_str = "∞ (inacessível)"
            else:
                dist_str = f"{dist:.0f} km"
            print(f"  {v:2d}. {g.cidades[v]:20s} | Distância: {dist_str:15s} | Rota: {caminho}")

        # 6. Consulta específica selecionada pelo usuário
        print(f"\n{'='*60}")
        print("RESULTADO DA CONSULTA")
        print(f"{'='*60}")
        caminho_especifico = reconstruir_caminho(predecessores, g.cidades, origem, destino)
        dist_total = distancias[destino]
        
        if dist_total == float('inf'):
            print(f"\n❌ Não há caminho disponível de {g.cidades[origem]} para {g.cidades[destino]}")
        else:
            print(f"\n✓ Melhor caminho de {g.cidades[origem]} para {g.cidades[destino]}:")
            print(f"  Rota: {caminho_especifico}")
            print(f"  Distância total: {dist_total:.0f} km")
            
            # 7. Visualizar o grafo
            print(f"\n{'='*60}")
            print("VISUALIZANDO GRAFO...")
            print(f"{'='*60}\n")
            g.visualizar_grafo(predecessores, origem, destino)