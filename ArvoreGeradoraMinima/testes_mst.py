"""
Testes automatizados para MST - Kruskal, Prim e UnionFind
"""

from mst_cidades import GrafoMST, UnionFind, Aresta, criar_mapa_brasil_ponderado


def teste_union_find():
    """Testa a estrutura UnionFind."""
    print("\n" + "="*70)
    print("TESTE 1: Union-Find")
    print("="*70)

    uf = UnionFind({"A", "B", "C", "D"})

    print("\n[OK] Inicializacao:")
    assert not uf.sao_conectados("A", "B"), "A e B nao devem estar conectados"
    print("  A e B estao desconectados [OK]")

    print("\n[OK] Union A-B:")
    uf.union("A", "B")
    assert uf.sao_conectados("A", "B"), "A e B devem estar conectados"
    print("  A e B estao conectados [OK]")

    print("\n[OK] Union B-C (transitividade):")
    uf.union("B", "C")
    assert uf.sao_conectados("A", "C"), "A e C devem estar conectados (transitivo)"
    print("  A e C estao conectados (transitivo) [OK]")

    print("\n[OK] D desconexo:")
    assert not uf.sao_conectados("A", "D"), "A e D nao devem estar conectados"
    print("  D continua desconectado [OK]")

    print("\n[PASSOU] TESTE 1: UnionFind - PASSOU\n")


def teste_grafo_simples():
    """Testa com um grafo pequeno e simples."""
    print("\n" + "="*70)
    print("TESTE 2: Grafo Simples (4 vértices)")
    print("="*70)

    grafo = GrafoMST()
    grafo.adicionar_estrada("A", "B", 1)
    grafo.adicionar_estrada("B", "C", 2)
    grafo.adicionar_estrada("C", "D", 3)
    grafo.adicionar_estrada("D", "A", 4)
    grafo.adicionar_estrada("A", "C", 5)

    print("\n🔄 Executando Kruskal...")
    resultado_k = grafo.kruskal()
    assert resultado_k is not None, "Kruskal deve encontrar MST"
    arestas_k, peso_k = resultado_k

    print(f"✓ Kruskal encontrou: {len(arestas_k)} arestas, peso = {peso_k}")

    assert len(arestas_k) == len(grafo.cidades) - 1, "Deve ter V-1 arestas"
    print(f"✓ Número de arestas correto: {len(arestas_k)} = 4-1")

    assert peso_k == 6, f"Peso deve ser 6, não {peso_k}"
    print(f"✓ Peso correto: {peso_k} km")

    print(f"\n🔄 Executando Prim...")
    resultado_p = grafo.prim("A")
    assert resultado_p is not None, "Prim deve encontrar MST"
    arestas_p, peso_p = resultado_p

    print(f"✓ Prim encontrou: {len(arestas_p)} arestas, peso = {peso_p}")

    assert peso_k == peso_p, f"Pesos devem ser iguais: {peso_k} vs {peso_p}"
    print(f"✓ Mesma MST: peso {peso_k} = {peso_p}")

    print("\n✅ TESTE 2: Grafo Simples - PASSOU\n")


def teste_grafo_brasil():
    """Testa com o grafo Brasil completo."""
    print("\n" + "="*70)
    print("TESTE 3: Grafo Brasil (20 vértices)")
    print("="*70)

    print("\n🔨 Construindo mapa...")
    grafo = criar_mapa_brasil_ponderado()

    assert len(grafo.cidades) >= 20, f"Deve ter pelo menos 20 cidades, tem {len(grafo.cidades)}"
    print(f"✓ Número correto de cidades: {len(grafo.cidades)}")

    assert len(grafo.arestas) == 28, f"Deve ter 28 arestas, tem {len(grafo.arestas)}"
    print(f"✓ Número correto de arestas: {len(grafo.arestas)}")

    print("\n🔄 Executando Kruskal...")
    resultado_k = grafo.kruskal()
    assert resultado_k is not None, "Kruskal deve encontrar MST"
    arestas_k, peso_k = resultado_k

    print(f"✓ Kruskal: {len(arestas_k)} arestas, peso = {peso_k:.1f} km")

    assert len(arestas_k) == len(grafo.cidades) - 1, f"Deve ter {len(grafo.cidades)-1} arestas, tem {len(arestas_k)}"
    print(f"✓ Número correto: {len(arestas_k)} = {len(grafo.cidades)}-1")

    print("\n🔄 Executando Prim...")
    resultado_p = grafo.prim("São Paulo")
    assert resultado_p is not None, "Prim deve encontrar MST"
    arestas_p, peso_p = resultado_p

    print(f"✓ Prim: {len(arestas_p)} arestas, peso = {peso_p:.1f} km")

    assert abs(peso_k - peso_p) < 0.01, f"Pesos devem ser iguais: {peso_k} vs {peso_p}"
    print(f"✓ Mesma MST: ambos peso = {peso_k:.1f} km")

    peso_total_grafo = sum(a.peso for a in grafo.arestas)
    economia = peso_total_grafo - peso_k
    economia_percent = (economia / peso_total_grafo) * 100

    print(f"\n📊 Análise:")
    print(f"   Todas as arestas: {peso_total_grafo:.1f} km")
    print(f"   MST: {peso_k:.1f} km")
    print(f"   Economia: {economia:.1f} km ({economia_percent:.1f}%)")

    assert economia > 0, "Deve ter economia positiva"
    print(f"✓ Economia positiva ✓")

    print("\n✅ TESTE 3: Grafo Brasil - PASSOU\n")


def teste_ciclos():
    """Testa a detecção de ciclos."""
    print("\n" + "="*70)
    print("TESTE 4: Detecção de Ciclos")
    print("="*70)

    grafo = GrafoMST()
    grafo.adicionar_estrada("A", "B", 1)
    grafo.adicionar_estrada("B", "C", 1)
    grafo.adicionar_estrada("C", "A", 1)

    print("\n🔍 Grafo com triângulo (3 arestas iguais):")
    print("   A ---- 1 ---- B")
    print("   |             |")
    print("   1             1")
    print("   |             |")
    print("   C ----------- (ciclo)")

    resultado = grafo.kruskal()
    arestas_mst, peso = resultado

    assert len(arestas_mst) == 2, f"MST deve ter 2 arestas (V-1), não {len(arestas_mst)}"
    print(f"\n✓ MST tem 2 arestas (evitou o ciclo)")
    print(f"✓ Peso MST: {peso} (deveria ser 2)")
    assert peso == 2, f"Peso deve ser 2, não {peso}"

    print("\n✅ TESTE 4: Detecção de Ciclos - PASSOU\n")


def teste_vertices_diferentes():
    """Testa Prim começando de vértices diferentes."""
    print("\n" + "="*70)
    print("TESTE 5: Prim com Vértices Iniciais Diferentes")
    print("="*70)

    print("\n🔨 Construindo mapa...")
    grafo = criar_mapa_brasil_ponderado()

    cidades_teste = ["São Paulo", "Rio de Janeiro", "Salvador"]
    pesos = []

    for cidade in cidades_teste:
        print(f"\n🔄 Prim começando de {cidade}...")
        resultado = grafo.prim(cidade)
        if resultado:
            arestas, peso = resultado
            pesos.append(peso)
            print(f"✓ Peso: {peso:.1f} km")

    for peso in pesos:
        assert abs(peso - pesos[0]) < 0.01, "Peso deve ser o mesmo independente do vértice inicial"

    print(f"\n✓ Todos resultados têm o mesmo peso: {pesos[0]:.1f} km")
    print("✓ Resultado independente do vértice inicial ✓")

    print("\n✅ TESTE 5: Vértices Diferentes - PASSOU\n")


def teste_aresta_menor_primeiro():
    """Verifica que Kruskal adiciona arestas menores primeiro."""
    print("\n" + "="*70)
    print("TESTE 6: Kruskal Ordena por Peso")
    print("="*70)

    grafo = GrafoMST()

    grafo.adicionar_estrada("A", "B", 5)
    grafo.adicionar_estrada("B", "C", 2)
    grafo.adicionar_estrada("C", "D", 1)
    grafo.adicionar_estrada("D", "A", 4)
    grafo.adicionar_estrada("A", "C", 3)

    print("\n📝 Arestas adicionadas em ordem: 5, 2, 1, 4, 3")

    resultado = grafo.kruskal()
    arestas_mst, peso = resultado

    arestas_ordenadas = sorted(arestas_mst, key=lambda a: a.peso)

    print(f"\n✓ MST encontrada com arestas:")
    for i, a in enumerate(arestas_ordenadas, 1):
        print(f"   {i}. {a.origem}-{a.destino}: {a.peso}")

    pesos_esperados = [1, 2, 3]
    pesos_reais = sorted([a.peso for a in arestas_mst])

    assert pesos_reais == pesos_esperados, f"Pesos: {pesos_reais} ≠ {pesos_esperados}"
    print(f"\n✓ Arestas menores foram selecionadas primeiro")

    print("\n✅ TESTE 6: Ordenação de Peso - PASSOU\n")


def executar_todos_testes():
    """Executa todos os testes."""
    print("\n" + "="*70)
    print("INICIANDO SUITE DE TESTES - MST")
    print("="*70)

    try:
        teste_union_find()
        teste_grafo_simples()
        teste_ciclos()
        teste_vertices_diferentes()
        teste_aresta_menor_primeiro()
        teste_grafo_brasil()

        print("\n" + "="*70)
        print("TODOS OS TESTES PASSARAM!")
        print("="*70)
        print("\nImplementação de MST está correta!")
        print("Kruskal: OK")
        print("Prim: OK")
        print("UnionFind: OK")
        print("Detecção de ciclos: OK")
        print("="*70 + "\n")

    except AssertionError as e:
        print(f"\nERRO: {e}")
        print("="*70 + "\n")
        return False

    return True


if __name__ == "__main__":
    executar_todos_testes()
