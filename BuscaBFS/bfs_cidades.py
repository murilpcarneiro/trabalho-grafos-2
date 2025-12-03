"""
Algoritmo BFS (Breadth-First Search - Busca em Largura)
Problema: Encontrar o caminho mais curto entre duas cidades
"""

from collections import deque
from typing import Dict, List, Set, Tuple, Optional


class GrafoCidades:
    # Grafo não-direcionado de cidades conectadas por estradas
    # Representado por lista de adjacências

    def __init__(self):
        # grafo: dicionário onde chave é cidade e valor é lista de vizinhos
        self.grafo: Dict[str, List[str]] = {}

    def adicionar_cidade(self, cidade: str) -> None:
        # Adiciona uma nova cidade (vértice) ao grafo
        if cidade not in self.grafo:
            self.grafo[cidade] = []
            print(f"✓ Cidade '{cidade}' adicionada ao mapa")

    def adicionar_estrada(self, cidade1: str, cidade2: str) -> None:
        # Adiciona uma estrada (aresta) bidirecional entre duas cidades
        # Grafo não-direcionado: conexão em ambas as direções
        if cidade1 not in self.grafo:
            self.adicionar_cidade(cidade1)
        if cidade2 not in self.grafo:
            self.adicionar_cidade(cidade2)

        # Adiciona conexão bidirecional
        if cidade2 not in self.grafo[cidade1]:
            self.grafo[cidade1].append(cidade2)
        if cidade1 not in self.grafo[cidade2]:
            self.grafo[cidade2].append(cidade1)

        print(f"✓ Estrada conectada: {cidade1} ↔ {cidade2}")

    def exibir_mapa(self) -> None:
        # Exibe todas as conexões do mapa de forma organizada
        print("\n" + "="*70)
        print("MAPA DE CONEXÕES ENTRE CIDADES")
        print("="*70)

        for cidade, vizinhos in sorted(self.grafo.items()):
            vizinhos_str = ", ".join(sorted(vizinhos))
            print(f"{cidade:20} → {vizinhos_str}")

        print("="*70)
        print(f"Total de cidades: {len(self.grafo)}")
        total_conexoes = sum(len(v) for v in self.grafo.values()) // 2
        print(f"Total de estradas: {total_conexoes}")
        print("="*70 + "\n")

    def bfs_caminho_mais_curto(self, origem: str, destino: str) -> Optional[Tuple[List[str], int]]:
        # Encontra o caminho mais curto entre duas cidades usando BFS (Busca em Largura)
        # Explora em camadas (nível 1, nível 2, etc) até encontrar o destino
        # Estruturas: Fila (deque) para FIFO, visitados (set) para marcar explorados, pais (dict) para reconstruir caminho
        # Retorna tupla (caminho, distancia) ou None se não houver caminho

        # ===== VALIDAÇÕES INICIAIS =====
        if origem not in self.grafo:
            print(f"❌ ERRO: Cidade de origem '{origem}' não existe no mapa!")
            return None

        if destino not in self.grafo:
            print(f"❌ ERRO: Cidade de destino '{destino}' não existe no mapa!")
            return None

        if origem == destino:
            print(f"✓ Origem e destino são a mesma cidade!")
            return ([origem], 0)

        # ===== INICIALIZAÇÃO DAS ESTRUTURAS =====

        # Fila para armazenar as cidades a serem exploradas
        # Começamos com a cidade de origem
        fila = deque([origem])

        # Conjunto para marcar cidades já visitadas (evita ciclos infinitos)
        visitados: Set[str] = {origem}

        # Dicionário para rastrear de onde viemos
        # Permite reconstruir o caminho depois
        pais: Dict[str, str] = {origem: None}

        print(f"\n🔍 Iniciando busca BFS de '{origem}' para '{destino}'...")
        print("─" * 70)

        nivel = 0  # Contador de níveis para visualização

        # ===== LOOP PRINCIPAL DO BFS =====
        while fila:
            # Processa todas as cidades do nível atual
            tamanho_nivel = len(fila)
            nivel += 1

            print(f"\n📍 NÍVEL {nivel}: Explorando {tamanho_nivel} cidade(s)...")

            for _ in range(tamanho_nivel):
                # Remove a primeira cidade da fila (FIFO)
                cidade_atual = fila.popleft()
                print(f"   → Visitando: {cidade_atual}")

                # ===== VERIFICA SE CHEGAMOS AO DESTINO =====
                if cidade_atual == destino:
                    print(f"\n✓ DESTINO ENCONTRADO! '{destino}' alcançado no nível {nivel}")
                    print("─" * 70)

                    # Reconstrói o caminho usando o dicionário 'pais'
                    caminho = []
                    atual = destino

                    # Volta do destino até a origem
                    while atual is not None:
                        caminho.append(atual)
                        atual = pais[atual]

                    # Inverte para ter o caminho origem -> destino
                    caminho.reverse()

                    # Distância = número de arestas = número de cidades - 1
                    distancia = len(caminho) - 1

                    return (caminho, distancia)

                # ===== EXPLORA OS VIZINHOS DA CIDADE ATUAL =====
                vizinhos_nao_visitados = []

                for vizinho in self.grafo[cidade_atual]:
                    # Se o vizinho ainda não foi visitado
                    if vizinho not in visitados:
                        # Marca como visitado
                        visitados.add(vizinho)

                        # Adiciona à fila para explorar depois
                        fila.append(vizinho)

                        # Registra que chegamos em 'vizinho' vindo de 'cidade_atual'
                        pais[vizinho] = cidade_atual

                        vizinhos_nao_visitados.append(vizinho)

                if vizinhos_nao_visitados:
                    print(f"      Novos vizinhos adicionados: {', '.join(vizinhos_nao_visitados)}")

        # ===== CAMINHO NÃO ENCONTRADO =====
        print(f"\n❌ Não existe caminho entre '{origem}' e '{destino}'")
        print("─" * 70)
        return None

    def exibir_resultado(self, origem: str, destino: str) -> None:
        # Executa o BFS e exibe o resultado formatado com origem, destino e caminho encontrado
        print("\n" + "="*70)
        print("SISTEMA DE NAVEGAÇÃO - BFS")
        print("="*70)
        print(f"🚗 Origem:  {origem}")
        print(f"🎯 Destino: {destino}")
        print("="*70)

        resultado = self.bfs_caminho_mais_curto(origem, destino)

        if resultado:
            caminho, distancia = resultado

            print("\n" + "="*70)
            print("RESULTADO DA BUSCA")
            print("="*70)
            print(f"✓ Caminho encontrado com sucesso!")
            print(f"📏 Distância: {distancia} conexão(ões)")
            print(f"🗺️  Caminho completo:")
            print()

            # Exibe o caminho de forma visual
            for i, cidade in enumerate(caminho):
                if i == 0:
                    print(f"   🚗 {cidade} (INÍCIO)")
                elif i == len(caminho) - 1:
                    print(f"   🎯 {cidade} (FIM)")
                else:
                    print(f"   {i}. {cidade}")

            print("\n" + "="*70 + "\n")


def criar_mapa_brasil() -> GrafoCidades:
    # Cria um mapa com 20 cidades brasileiras (mínimo 16) e suas conexões representando estradas
    print("\n" + "="*70)
    print("CONSTRUINDO MAPA DE CIDADES BRASILEIRAS")
    print("="*70 + "\n")

    mapa = GrafoCidades()

    # Lista de conexões (estradas) entre cidades
    # Formato: (cidade1, cidade2)
    conexoes = [
        # Região Sudeste - Hub principal
        ("São Paulo", "Rio de Janeiro"),
        ("São Paulo", "Belo Horizonte"),
        ("São Paulo", "Curitiba"),
        ("São Paulo", "Campinas"),
        ("Rio de Janeiro", "Belo Horizonte"),
        ("Rio de Janeiro", "Vitória"),
        ("Campinas", "Belo Horizonte"),

        # Região Sul
        ("Curitiba", "Florianópolis"),
        ("Curitiba", "Porto Alegre"),
        ("Florianópolis", "Porto Alegre"),

        # Região Centro-Oeste
        ("Belo Horizonte", "Brasília"),
        ("São Paulo", "Campo Grande"),
        ("Brasília", "Goiânia"),
        ("Goiânia", "Campo Grande"),
        ("Campo Grande", "Cuiabá"),

        # Região Nordeste
        ("Brasília", "Salvador"),
        ("Salvador", "Recife"),
        ("Salvador", "Fortaleza"),
        ("Recife", "Fortaleza"),
        ("Recife", "Natal"),
        ("Fortaleza", "Natal"),
        ("Fortaleza", "Teresina"),
        ("Teresina", "São Luís"),

        # Região Norte
        ("Brasília", "Palmas"),
        ("Palmas", "Belém"),
        ("Belém", "São Luís"),
        ("Palmas", "Manaus"),
        ("Belém", "Manaus"),
    ]

    # Adiciona todas as conexões ao mapa
    for cidade1, cidade2 in conexoes:
        mapa.adicionar_estrada(cidade1, cidade2)

    print()
    return mapa


def menu_principal():
    # Interface principal com menu interativo para buscar caminhos entre cidades
    print("\n" + "="*70)
    print(" "*15 + "BFS - SISTEMA DE NAVEGAÇÃO ENTRE CIDADES")
    print("="*70)

    # Cria o mapa de cidades
    mapa = criar_mapa_brasil()

    # Exibe o mapa completo
    mapa.exibir_mapa()

    while True:
        print("\n" + "─"*70)
        print("MENU DE OPÇÕES")
        print("─"*70)
        print("1. Buscar caminho mais curto entre duas cidades")
        print("2. Ver mapa de conexões novamente")
        print("3. Exemplos de buscas pré-definidas")
        print("4. Sair")
        print("─"*70)

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            print("\n📍 Cidades disponíveis:")
            cidades = sorted(mapa.grafo.keys())
            for i, cidade in enumerate(cidades, 1):
                print(f"   {i:2d}. {cidade}")

            origem_input = input("\n🚗 Digite o NÚMERO ou NOME da cidade de ORIGEM: ").strip()
            destino_input = input("🎯 Digite o NÚMERO ou NOME da cidade de DESTINO: ").strip()

            # Converte número para nome da cidade se necessário
            try:
                num_origem = int(origem_input)
                if 1 <= num_origem <= len(cidades):
                    origem = cidades[num_origem - 1]
                else:
                    print(f"❌ Número inválido! Escolha entre 1 e {len(cidades)}")
                    continue
            except ValueError:
                origem = origem_input

            try:
                num_destino = int(destino_input)
                if 1 <= num_destino <= len(cidades):
                    destino = cidades[num_destino - 1]
                else:
                    print(f"❌ Número inválido! Escolha entre 1 e {len(cidades)}")
                    continue
            except ValueError:
                destino = destino_input

            mapa.exibir_resultado(origem, destino)

        elif opcao == "2":
            mapa.exibir_mapa()

        elif opcao == "3":
            print("\n" + "="*70)
            print("EXEMPLOS DE BUSCAS")
            print("="*70)

            exemplos = [
                ("Manaus", "Porto Alegre"),
                ("São Paulo", "Fortaleza"),
                ("Rio de Janeiro", "Cuiabá")
            ]

            for origem, destino in exemplos:
                input(f"\nPressione ENTER para buscar: {origem} → {destino}")
                mapa.exibir_resultado(origem, destino)

        elif opcao == "4":
            print("\n" + "="*70)
            print("Obrigado por usar o Sistema de Navegação BFS!")
            print("="*70 + "\n")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")


# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Executa o programa principal.

    Para executar este programa:
    1. Certifique-se de ter Python 3.7+ instalado
    2. Execute: python bfs_cidades.py
    3. Siga as instruções do menu interativo
    """
    menu_principal()
