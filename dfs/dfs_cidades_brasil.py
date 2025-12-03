"""
ALGORITMO DFS (DEPTH-FIRST SEARCH) - BUSCA EM PROFUNDIDADE
Aplicação: Mapeamento e Exploração de Cidades Brasileiras

Este programa implementa o algoritmo DFS para explorar conexões entre cidades brasileiras,
simulando rotas de transporte e conexões regionais.

Características:
- Grafo com mais de 16 vértices (cidades)
- Busca em profundidade recursiva e iterativa
- Visualização do grafo
- Detecção de componentes conectados
- Identificação de ciclos
"""

import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple


class GrafoCidadesBrasil:
    """
    Classe que representa um grafo de cidades brasileiras usando lista de adjacências.
    
    Atributos:
        grafo: Dicionário onde a chave é a cidade e o valor é uma lista de cidades conectadas
        num_vertices: Número total de cidades no grafo
    """
    
    def __init__(self):
        """Inicializa o grafo como um dicionário de listas de adjacências."""
        self.grafo = defaultdict(list)
        self.num_vertices = 0
        self.cidades = set()
    
    def adicionar_aresta(self, cidade1: str, cidade2: str, bidirecional: bool = True):
        """
        Adiciona uma conexão (aresta) entre duas cidades.
        
        Args:
            cidade1: Cidade de origem
            cidade2: Cidade de destino
            bidirecional: Se True, cria conexão nos dois sentidos (grafo não-direcionado)
        """
        self.grafo[cidade1].append(cidade2)
        self.cidades.add(cidade1)
        self.cidades.add(cidade2)
        
        if bidirecional:
            self.grafo[cidade2].append(cidade1)
        
        self.num_vertices = len(self.cidades)
    
    def dfs_recursivo(self, cidade_inicial: str, visitados: Set[str] = None, caminho: List[str] = None) -> List[str]:
        """
        Implementação RECURSIVA do algoritmo DFS.
        
        O DFS explora o grafo indo o mais fundo possível em cada ramo antes de retroceder.
        
        Complexidade de Tempo: O(V + E) onde V = vértices e E = arestas
        Complexidade de Espaço: O(V) para a pilha de recursão e conjunto de visitados
        
        Args:
            cidade_inicial: Cidade de onde a busca começa
            visitados: Conjunto de cidades já visitadas
            caminho: Lista que armazena a ordem de visitação
            
        Returns:
            Lista com a ordem de visitação das cidades
        """
        # Inicializa estruturas se for a primeira chamada
        if visitados is None:
            visitados = set()
        if caminho is None:
            caminho = []
        
        # Marca a cidade atual como visitada
        visitados.add(cidade_inicial)
        caminho.append(cidade_inicial)
        
        print(f"Visitando: {cidade_inicial}")
        
        # Explora recursivamente todas as cidades adjacentes não visitadas
        for cidade_vizinha in self.grafo[cidade_inicial]:
            if cidade_vizinha not in visitados:
                self.dfs_recursivo(cidade_vizinha, visitados, caminho)
        
        return caminho
    
    def dfs_iterativo(self, cidade_inicial: str) -> List[str]:
        """
        Implementação ITERATIVA do algoritmo DFS usando uma pilha explícita.
        
        Esta versão usa uma estrutura de dados pilha (stack) em vez de recursão.
        É útil para evitar estouro de pilha em grafos muito grandes.
        
        Complexidade de Tempo: O(V + E)
        Complexidade de Espaço: O(V)
        
        Args:
            cidade_inicial: Cidade de onde a busca começa
            
        Returns:
            Lista com a ordem de visitação das cidades
        """
        visitados = set()
        caminho = []
        pilha = [cidade_inicial]  # Pilha para controlar a exploração
        
        print("\n=== DFS ITERATIVO ===")
        
        while pilha:
            # Remove o topo da pilha
            cidade_atual = pilha.pop()
            
            # Se ainda não foi visitada, processa
            if cidade_atual not in visitados:
                visitados.add(cidade_atual)
                caminho.append(cidade_atual)
                print(f"Visitando: {cidade_atual}")
                
                # Adiciona vizinhos não visitados à pilha (em ordem reversa para manter a ordem)
                for cidade_vizinha in reversed(self.grafo[cidade_atual]):
                    if cidade_vizinha not in visitados:
                        pilha.append(cidade_vizinha)
        
        return caminho
    
    def dfs_completo(self) -> Dict[int, List[str]]:
        """
        Executa DFS em todos os componentes conectados do grafo.
        
        Útil para grafos desconexos, onde existem grupos de cidades isolados.
        
        Returns:
            Dicionário onde cada chave é um componente e o valor é a lista de cidades
        """
        visitados = set()
        componentes = {}
        num_componente = 0
        
        print("\n=== DFS COMPLETO - TODOS OS COMPONENTES ===")
        
        for cidade in self.cidades:
            if cidade not in visitados:
                print(f"\nComponente {num_componente + 1}:")
                caminho = []
                self._dfs_auxiliar(cidade, visitados, caminho)
                componentes[num_componente] = caminho
                num_componente += 1
        
        return componentes
    
    def _dfs_auxiliar(self, cidade: str, visitados: Set[str], caminho: List[str]):
        """Função auxiliar recursiva para DFS completo."""
        visitados.add(cidade)
        caminho.append(cidade)
        print(f"  - {cidade}")
        
        for vizinho in self.grafo[cidade]:
            if vizinho not in visitados:
                self._dfs_auxiliar(vizinho, visitados, caminho)
    
    def encontrar_caminho_dfs(self, origem: str, destino: str) -> List[str]:
        """
        Usa DFS para encontrar um caminho entre duas cidades.
        
        Args:
            origem: Cidade de partida
            destino: Cidade de chegada
            
        Returns:
            Lista representando o caminho encontrado, ou lista vazia se não existe
        """
        visitados = set()
        caminho = []
        
        if self._dfs_caminho_auxiliar(origem, destino, visitados, caminho):
            return caminho
        return []
    
    def _dfs_caminho_auxiliar(self, atual: str, destino: str, visitados: Set[str], caminho: List[str]) -> bool:
        """Função auxiliar recursiva para encontrar caminho."""
        visitados.add(atual)
        caminho.append(atual)
        
        # Se chegou ao destino, retorna True
        if atual == destino:
            return True
        
        # Explora vizinhos
        for vizinho in self.grafo[atual]:
            if vizinho not in visitados:
                if self._dfs_caminho_auxiliar(vizinho, destino, visitados, caminho):
                    return True
        
        # Se não encontrou o caminho, remove da lista (backtracking)
        caminho.pop()
        return False
    
    def detectar_ciclo(self) -> bool:
        """
        Detecta se existe algum ciclo no grafo usando DFS.
        
        Returns:
            True se existe ciclo, False caso contrário
        """
        visitados = set()
        pilha_recursao = set()
        
        for cidade in self.cidades:
            if cidade not in visitados:
                if self._detectar_ciclo_auxiliar(cidade, visitados, pilha_recursao, None):
                    return True
        return False
    
    def _detectar_ciclo_auxiliar(self, cidade: str, visitados: Set[str], pilha_recursao: Set[str], pai: str) -> bool:
        """Função auxiliar para detectar ciclos."""
        visitados.add(cidade)
        pilha_recursao.add(cidade)
        
        for vizinho in self.grafo[cidade]:
            if vizinho not in visitados:
                if self._detectar_ciclo_auxiliar(vizinho, visitados, pilha_recursao, cidade):
                    return True
            elif vizinho in pilha_recursao and vizinho != pai:
                return True
        
        pilha_recursao.remove(cidade)
        return False
    
    def visualizar_grafo(self, titulo: str = "Grafo de Cidades Brasileiras", caminho_destaque: List[str] = None):
        """
        Visualiza o grafo usando matplotlib e networkx.
        
        Args:
            titulo: Título do gráfico
            caminho_destaque: Lista de cidades para destacar (resultado do DFS)
        """
        # Cria o grafo networkx
        G = nx.Graph()
        
        # Adiciona arestas
        for cidade, vizinhos in self.grafo.items():
            for vizinho in vizinhos:
                G.add_edge(cidade, vizinho)
        
        # Configuração da visualização
        plt.figure(figsize=(18, 14))
        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
        
        # Desenha todas as arestas do grafo em cinza claro
        nx.draw_networkx_edges(G, pos, alpha=0.2, width=1.5, edge_color='gray')
        
        # Destaca o caminho DFS se fornecido
        if caminho_destaque and len(caminho_destaque) > 1:
            # Cria arestas do caminho percorrido pelo DFS
            caminho_arestas = []
            for i in range(len(caminho_destaque)-1):
                if caminho_destaque[i+1] in self.grafo[caminho_destaque[i]]:
                    caminho_arestas.append((caminho_destaque[i], caminho_destaque[i+1]))
            
            # Desenha as arestas do caminho DFS em vermelho (ordem de exploração)
            nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, 
                                  edge_color='red', width=4, alpha=0.8,
                                  arrows=True, arrowsize=20, arrowstyle='->')
            
            # Cria mapeamento de cores e tamanhos para os nós
            cores_nos = []
            tamanhos_nos = []
            for cidade in G.nodes():
                if cidade == caminho_destaque[0]:
                    cores_nos.append('lime')  # Cidade inicial - verde brilhante
                    tamanhos_nos.append(1500)
                elif cidade == caminho_destaque[-1]:
                    cores_nos.append('orange')  # Última cidade visitada - laranja
                    tamanhos_nos.append(1500)
                elif cidade in caminho_destaque:
                    cores_nos.append('lightcoral')  # Cidades visitadas pelo DFS - vermelho claro
                    tamanhos_nos.append(1200)
                else:
                    cores_nos.append('lightgray')  # Cidades não visitadas - cinza
                    tamanhos_nos.append(800)
            
            nx.draw_networkx_nodes(G, pos, node_color=cores_nos, 
                                  node_size=tamanhos_nos, alpha=0.9,
                                  edgecolors='black', linewidths=2)
            
            # Adiciona números de ordem de visitação
            labels_ordem = {}
            for idx, cidade in enumerate(caminho_destaque, 1):
                labels_ordem[cidade] = f"{cidade}\n[{idx}]"
            
            # Labels para cidades não visitadas
            for cidade in G.nodes():
                if cidade not in caminho_destaque:
                    labels_ordem[cidade] = cidade
            
            nx.draw_networkx_labels(G, pos, labels_ordem, font_size=7, font_weight='bold')
            
            # Adiciona legenda
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor='lime', edgecolor='black', label='Cidade Inicial'),
                Patch(facecolor='lightcoral', edgecolor='black', label='Visitadas (ordem DFS)'),
                Patch(facecolor='orange', edgecolor='black', label='Última Visitada'),
                Patch(facecolor='lightgray', edgecolor='black', label='Não Visitadas')
            ]
            plt.legend(handles=legend_elements, loc='upper left', fontsize=10)
            
        else:
            # Desenha todos os nós normalmente
            nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                                  node_size=1000, alpha=0.9,
                                  edgecolors='black', linewidths=2)
            nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
        
        plt.title(titulo, fontsize=18, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def estatisticas(self):
        """Exibe estatísticas do grafo."""
        print("\n" + "="*60)
        print("ESTATÍSTICAS DO GRAFO")
        print("="*60)
        print(f"Número de cidades (vértices): {self.num_vertices}")
        
        total_conexoes = sum(len(vizinhos) for vizinhos in self.grafo.values()) // 2
        print(f"Número de conexões (arestas): {total_conexoes}")
        
        # Grau médio
        graus = [len(self.grafo[cidade]) for cidade in self.cidades]
        grau_medio = sum(graus) / len(graus) if graus else 0
        print(f"Grau médio: {grau_medio:.2f}")
        
        # Cidade com mais conexões
        cidade_max = max(self.cidades, key=lambda c: len(self.grafo[c]))
        print(f"Cidade com mais conexões: {cidade_max} ({len(self.grafo[cidade_max])} conexões)")
        
        # Verifica ciclos
        tem_ciclo = self.detectar_ciclo()
        print(f"Possui ciclos: {'Sim' if tem_ciclo else 'Não'}")
        print("="*60)


def criar_grafo_brasil():
    """
    Cria um grafo representando conexões entre cidades brasileiras.
    
    O grafo representa rotas de transporte (rodoviárias, aéreas) entre principais cidades
    de diferentes regiões do Brasil, totalizando mais de 16 vértices conforme requisito.
    
    Returns:
        GrafoCidadesBrasil: Objeto do grafo populado
    """
    grafo = GrafoCidadesBrasil()
    
    # REGIÃO SUDESTE - Hub econômico
    grafo.adicionar_aresta("São Paulo", "Rio de Janeiro")
    grafo.adicionar_aresta("São Paulo", "Belo Horizonte")
    grafo.adicionar_aresta("São Paulo", "Campinas")
    grafo.adicionar_aresta("Rio de Janeiro", "Belo Horizonte")
    grafo.adicionar_aresta("Belo Horizonte", "Vitória")
    grafo.adicionar_aresta("Campinas", "Ribeirão Preto")
    
    # REGIÃO SUL
    grafo.adicionar_aresta("Curitiba", "Florianópolis")
    grafo.adicionar_aresta("Curitiba", "Porto Alegre")
    grafo.adicionar_aresta("Florianópolis", "Porto Alegre")
    grafo.adicionar_aresta("São Paulo", "Curitiba")
    
    # REGIÃO CENTRO-OESTE
    grafo.adicionar_aresta("Brasília", "Goiânia")
    grafo.adicionar_aresta("Brasília", "Campo Grande")
    grafo.adicionar_aresta("Brasília", "Cuiabá")
    grafo.adicionar_aresta("Goiânia", "Cuiabá")
    grafo.adicionar_aresta("Belo Horizonte", "Brasília")
    grafo.adicionar_aresta("São Paulo", "Brasília")
    
    # REGIÃO NORDESTE
    grafo.adicionar_aresta("Salvador", "Recife")
    grafo.adicionar_aresta("Salvador", "Fortaleza")
    grafo.adicionar_aresta("Recife", "Fortaleza")
    grafo.adicionar_aresta("Recife", "Natal")
    grafo.adicionar_aresta("Salvador", "Aracaju")
    grafo.adicionar_aresta("Brasília", "Salvador")
    
    # REGIÃO NORTE
    grafo.adicionar_aresta("Manaus", "Belém")
    grafo.adicionar_aresta("Manaus", "Porto Velho")
    grafo.adicionar_aresta("Belém", "São Luís")
    grafo.adicionar_aresta("São Luís", "Fortaleza")
    grafo.adicionar_aresta("Brasília", "Manaus")
    grafo.adicionar_aresta("Cuiabá", "Porto Velho")
    
    return grafo


def main():
    """Função principal que demonstra o funcionamento do DFS."""
    
    print("="*60)
    print("ALGORITMO DFS - BUSCA EM PROFUNDIDADE")
    print("Aplicação: Exploração de Cidades Brasileiras")
    print("="*60)
    
    # Cria o grafo
    grafo = criar_grafo_brasil()
    
    # Exibe estatísticas
    grafo.estatisticas()
    
    # Demonstração 1: DFS Recursivo
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO 1: DFS RECURSIVO")
    print("="*60)
    cidade_inicial = "São Paulo"
    print(f"\nIniciando busca a partir de: {cidade_inicial}\n")
    caminho_recursivo = grafo.dfs_recursivo(cidade_inicial)
    print(f"\nOrdem de visitação (Recursivo): {' -> '.join(caminho_recursivo)}")
    print(f"Total de cidades visitadas: {len(caminho_recursivo)}")
    
    # Demonstração 2: DFS Iterativo
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO 2: DFS ITERATIVO")
    print("="*60)
    caminho_iterativo = grafo.dfs_iterativo(cidade_inicial)
    print(f"\nOrdem de visitação (Iterativo): {' -> '.join(caminho_iterativo)}")
    print(f"Total de cidades visitadas: {len(caminho_iterativo)}")
    
    # Demonstração 3: DFS para encontrar caminho
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO 3: ENCONTRAR CAMINHO ENTRE DUAS CIDADES")
    print("="*60)
    origem = "São Paulo"
    destino = "Manaus"
    caminho = grafo.encontrar_caminho_dfs(origem, destino)
    if caminho:
        print(f"\nCaminho encontrado de {origem} até {destino}:")
        print(" -> ".join(caminho))
        print(f"Distância: {len(caminho) - 1} conexões")
    else:
        print(f"\nNenhum caminho encontrado entre {origem} e {destino}")
    
    # Demonstração 4: DFS Completo (todos os componentes)
    componentes = grafo.dfs_completo()
    print(f"\nNúmero de componentes conectados: {len(componentes)}")
    
    # Demonstração 5: Visualização
    print("\n" + "="*60)
    print("GERANDO VISUALIZAÇÃO DO GRAFO...")
    print("="*60)
    
    # Visualiza grafo completo
    grafo.visualizar_grafo("Mapa de Conexões entre Cidades Brasileiras")
    
    # Visualiza com caminho DFS destacado
    grafo.visualizar_grafo(
        f"DFS a partir de {cidade_inicial}",
        caminho_recursivo
    )
    
    print("\n" + "="*60)
    print("EXECUÇÃO CONCLUÍDA!")
    print("="*60)


if __name__ == "__main__":
    main()
