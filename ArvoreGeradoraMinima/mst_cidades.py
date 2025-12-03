from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Aresta:
    # Representa uma aresta (estrada) com peso
    # origem: Primeira cidade
    # destino: Segunda cidade
    # peso: Custo/distância da estrada
    origem: str
    destino: str
    peso: float

    def __lt__(self, outro: 'Aresta') -> bool:
        # Compara arestas pelo peso para ordenação
        return self.peso < outro.peso

    def __le__(self, outro: 'Aresta') -> bool:
        # Compara arestas pelo peso para ordenação
        return self.peso <= outro.peso


class UnionFind:
    # Estrutura Union-Find para detectar ciclos no Kruskal
    # Utiliza compressão de caminho e union por rank para otimização

    def __init__(self, elementos: Set[str]) -> None:
        # pai: mapa de cada elemento para seu representante
        # rank: altura da árvore para otimizar operações
        self.pai: Dict[str, str] = {elem: elem for elem in elementos}
        self.rank: Dict[str, int] = {elem: 0 for elem in elementos}

    def find(self, x: str) -> str:
        # Encontra o representante do conjunto com compressão de caminho
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x: str, y: str) -> None:
        # Une dois conjuntos usando union por rank
        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x == raiz_y:
            return

        # Une por rank para manter a árvore balanceada
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1

    def sao_conectados(self, x: str, y: str) -> bool:
        # Verifica se dois elementos estão no mesmo conjunto
        return self.find(x) == self.find(y)


class GrafoMST:
    # Grafo ponderado não-direcionado para cálculo de MST
    # Suporta algoritmos de Kruskal e Prim

    def __init__(self):
        # arestas: lista de todas as arestas com pesos
        # adjacencias: dicionário de listas de adjacências
        # cidades: conjunto de vértices
        self.arestas: List[Aresta] = []
        self.adjacencias: Dict[str, List[Tuple[str, float]]] = {}
        self.cidades: Set[str] = set()

    def adicionar_cidade(self, cidade: str) -> None:
        # Adiciona uma nova cidade (vértice) ao grafo
        if cidade not in self.cidades:
            self.cidades.add(cidade)
            self.adjacencias[cidade] = []
            print(f"[OK] Cidade '{cidade}' adicionada")

    def adicionar_estrada(self, cidade1: str, cidade2: str, distancia: float) -> None:
        # Adiciona uma aresta (estrada) ponderada entre duas cidades
        if cidade1 not in self.cidades:
            self.adicionar_cidade(cidade1)
        if cidade2 not in self.cidades:
            self.adicionar_cidade(cidade2)

        aresta = Aresta(cidade1, cidade2, distancia)
        self.arestas.append(aresta)
        # Grafo não-direcionado: adiciona em ambas as direções
        self.adjacencias[cidade1].append((cidade2, distancia))
        self.adjacencias[cidade2].append((cidade1, distancia))
        print(f"[OK] Estrada: {cidade1} <-> {cidade2} ({distancia} km)")

    def exibir_grafo(self) -> None:
        # Exibe o grafo ponderado de forma organizada
        print("\n" + "="*70)
        print("MAPA DE ESTRADAS COM DISTÂNCIAS")
        print("="*70)

        for cidade in sorted(self.adjacencias.keys()):
            conexoes = self.adjacencias[cidade]
            if conexoes:
                conexoes_str = ", ".join(
                    f"{vizinho}({dist}km)" for vizinho, dist in sorted(conexoes)
                )
                print(f"{cidade:20} → {conexoes_str}")

        print("="*70)
        print(f"Total de cidades: {len(self.cidades)}")
        print(f"Total de arestas: {len(self.arestas)}")
        peso_total = sum(a.peso for a in self.arestas)
        print(f"Distância total de todas as estradas: {peso_total:.1f} km")
        print("="*70 + "\n")

    def kruskal(self) -> Optional[Tuple[List[Aresta], float]]:
        # ALGORITMO DE KRUSKAL - MST por ordenação de arestas
        # 1. Ordena arestas por peso
        # 2. Processa cada aresta se não criar ciclo
        # 3. Para quando tiver V-1 arestas

        print("\n" + "="*70)
        print("ALGORITMO DE KRUSKAL - ÁRVORE GERADORA MÍNIMA")
        print("="*70)

        if not self.arestas:
            print("ERRO: Grafo sem arestas!")
            return None

        # Ordena as arestas por peso (menor primeiro)
        arestas_ordenadas = sorted(self.arestas)
        print(f"\nTotal de arestas: {len(arestas_ordenadas)}")

        # Estrutura Union-Find para detectar ciclos
        uf = UnionFind(self.cidades)
        mst_arestas: List[Aresta] = []
        peso_total_mst = 0.0
        arestas_processadas = 0
        ciclos_evitados = 0

        # Processa cada aresta em ordem de peso
        for aresta in arestas_ordenadas:
            arestas_processadas += 1

            # Se não criar ciclo, adiciona à MST
            if not uf.sao_conectados(aresta.origem, aresta.destino):
                mst_arestas.append(aresta)
                peso_total_mst += aresta.peso
                uf.union(aresta.origem, aresta.destino)
                print(f"ADICIONA: {aresta.origem} ↔ {aresta.destino} ({aresta.peso:.1f} km)")
                # Para quando tiver V-1 arestas
                if len(mst_arestas) == len(self.cidades) - 1:
                    break
            else:
                # Aresta criaria ciclo, descarta
                ciclos_evitados += 1

        # Verifica se grafo é conexo
        if len(mst_arestas) != len(self.cidades) - 1:
            print(f"ERRO: Grafo não é totalmente conexo!")
            return None

        print(f"\nMST completa com {len(mst_arestas)} arestas")
        return (mst_arestas, peso_total_mst)

    def prim(self, inicio: Optional[str] = None) -> Optional[Tuple[List[Aresta], float]]:
        # ALGORITMO DE PRIM - MST por crescimento incremental
        # 1. Começa com um vértice
        # 2. Sempre adiciona a aresta de menor peso que conecta a MST a fora
        # 3. Expande até cobrir todos os vértices

        print("\n" + "="*70)
        print("ALGORITMO DE PRIM - ÁRVORE GERADORA MÍNIMA")
        print("="*70)

        if not self.cidades:
            print("ERRO: Grafo sem vértices!")
            return None

        # Define vértice inicial
        if inicio is None or inicio not in self.cidades:
            inicio = list(self.cidades)[0]

        # Vértices na MST e fora dela
        na_mst: Set[str] = {inicio}
        fora_da_mst: Set[str] = self.cidades - {inicio}
        mst_arestas: List[Aresta] = []
        peso_total_mst = 0.0
        etapa = 1

        # Expande a árvore até cobrir todos os vértices
        while fora_da_mst:
            etapa += 1
            # Encontra a aresta de menor peso conectando MST a fora
            melhor_aresta: Optional[Aresta] = None
            melhor_peso = float('inf')

            # Para cada vértice na MST
            for vertice_mst in na_mst:
                # Para cada vizinho desse vértice
                for vizinho, peso in self.adjacencias[vertice_mst]:
                    # Se vizinho está fora e tem menor peso
                    if vizinho in fora_da_mst and peso < melhor_peso:
                        melhor_aresta = Aresta(vertice_mst, vizinho, peso)
                        melhor_peso = peso

            # Adiciona a melhor aresta encontrada
            if melhor_aresta:
                mst_arestas.append(melhor_aresta)
                peso_total_mst += melhor_aresta.peso
                destino = melhor_aresta.destino
                na_mst.add(destino)
                fora_da_mst.remove(destino)
                print(f"Etapa {etapa}: Adiciona {melhor_aresta.origem} ↔ {destino} ({melhor_aresta.peso:.1f} km)")

        print(f"\nMST completa com {len(mst_arestas)} arestas")
        return (mst_arestas, peso_total_mst)

    def exibir_mst(self, mst_arestas: List[Aresta], peso_total: float,
                   nome_algoritmo: str) -> None:
        # Exibe a MST de forma formatada
        print(f"\nRESULTADO - MST ({nome_algoritmo})")
        print(f"Total de estradas: {len(mst_arestas)} | Distância: {peso_total:.1f} km")
        distancia_todas = sum(a.peso for a in self.arestas)
        economia = distancia_todas - peso_total
        economia_percent = (economia / distancia_todas) * 100
        print(f"Economia: {economia:.1f} km ({economia_percent:.1f}%)\n")


def criar_mapa_brasil_ponderado() -> GrafoMST:
    # Cria um mapa com cidades brasileiras e distâncias em km
    print("\nConstruindo mapa de cidades brasileiras...\n")

    grafo = GrafoMST()
    # Lista de conexões com distâncias em km
    conexoes = [
        # Região Sudeste - Hub principal
        ("São Paulo", "Rio de Janeiro", 430),
        ("São Paulo", "Belo Horizonte", 586),
        ("São Paulo", "Curitiba", 405),
        ("São Paulo", "Campinas", 99),
        ("Rio de Janeiro", "Belo Horizonte", 586),
        ("Rio de Janeiro", "Vitória", 521),
        ("Campinas", "Belo Horizonte", 750),

        # Região Sul
        ("Curitiba", "Florianópolis", 626),
        ("Curitiba", "Porto Alegre", 710),
        ("Florianópolis", "Porto Alegre", 473),

        # Região Centro-Oeste
        ("Belo Horizonte", "Brasília", 743),
        ("São Paulo", "Campo Grande", 1155),
        ("Brasília", "Goiânia", 209),
        ("Goiânia", "Campo Grande", 933),
        ("Campo Grande", "Cuiabá", 694),

        # Região Nordeste
        ("Brasília", "Salvador", 1401),
        ("Salvador", "Recife", 839),
        ("Salvador", "Fortaleza", 1254),
        ("Recife", "Fortaleza", 632),
        ("Recife", "Natal", 297),
        ("Fortaleza", "Natal", 541),
        ("Fortaleza", "Teresina", 622),
        ("Teresina", "São Luís", 363),

        # Região Norte
        ("Brasília", "Palmas", 897),
        ("Palmas", "Belém", 1476),
        ("Belém", "São Luís", 1180),
        ("Palmas", "Manaus", 2156),
        ("Belém", "Manaus", 1722),
    ]

    for cidade1, cidade2, distancia in conexoes:
        grafo.adicionar_estrada(cidade1, cidade2, distancia)
    print()
    return grafo


def menu_principal():
    # Menu interativo para executar algoritmos de MST
    print("\nMST - SISTEMA DE OTIMIZACAO DE ESTRADAS\n")
    grafo = criar_mapa_brasil_ponderado()
    grafo.exibir_grafo()

    while True:
        print("\n" + "─"*70)
        print("MENU DE OPÇÕES")
        print("─"*70)
        print("1. Executar Algoritmo de Kruskal")
        print("2. Executar Algoritmo de Prim")
        print("3. Comparar Kruskal vs Prim")
        print("4. Ver mapa de estradas novamente")
        print("5. Sair")
        print("─"*70)

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            resultado = grafo.kruskal()
            if resultado:
                mst_arestas, peso_total = resultado
                grafo.exibir_mst(mst_arestas, peso_total, "Kruskal")

        elif opcao == "2":
            print("\n🌳 Selecione a cidade inicial (ou deixe em branco para usar a primeira):")
            cidades = sorted(grafo.cidades)
            for i, cidade in enumerate(cidades, 1):
                print(f"   {i:2d}. {cidade}")

            inicio_input = input("\nDigite o NÚMERO ou NOME da cidade inicial: ").strip()

            inicio = None
            if inicio_input:
                try:
                    num = int(inicio_input)
                    if 1 <= num <= len(cidades):
                        inicio = cidades[num - 1]
                except ValueError:
                    inicio = inicio_input
            else:
                inicio = cidades[0]

            resultado = grafo.prim(inicio)
            if resultado:
                mst_arestas, peso_total = resultado
                grafo.exibir_mst(mst_arestas, peso_total, f"Prim (início: {inicio})")

        elif opcao == "3":
            print("\n" + "="*70)
            print("COMPARAÇÃO: KRUSKAL vs PRIM")
            print("="*70)

            resultado_k = grafo.kruskal()
            if resultado_k:
                arestas_k, peso_k = resultado_k
                grafo.exibir_mst(arestas_k, peso_k, "Kruskal")

            input("\nPressione ENTER para executar Prim...")
            resultado_p = grafo.prim()
            if resultado_p:
                arestas_p, peso_p = resultado_p
                grafo.exibir_mst(arestas_p, peso_p, "Prim")

            if resultado_k and resultado_p:
                print("\n" + "="*70)
                print("ANÁLISE COMPARATIVA")
                print("="*70)
                print(f"\n✓ Ambos os algoritmos encontram a MESMA MST (exceto ordem das arestas)")
                print(f"   Peso Kruskal: {peso_k:.1f} km")
                print(f"   Peso Prim:    {peso_p:.1f} km")
                print(f"   Diferença:    {abs(peso_k - peso_p):.1f} km")

                if abs(peso_k - peso_p) < 0.01:
                    print("\n✓ Os pesos são IDÊNTICOS! Ambos encontram a MST ótima.")

                print("\n📊 CARACTERÍSTICAS:")
                print("   Kruskal:")
                print("   - Ordena arestas primeiro")
                print("   - Melhor para grafos esparsos")
                print("   - Usa Union-Find para detectar ciclos")
                print("\n   Prim:")
                print("   - Cresce a árvore incrementalmente")
                print("   - Melhor para grafos densos")
                print("   - Começa de um vértice específico")
                print("="*70 + "\n")

        elif opcao == "4":
            grafo.exibir_grafo()
        elif opcao == "5":
            print("\nSaindo...\n")
            break
        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    menu_principal()
