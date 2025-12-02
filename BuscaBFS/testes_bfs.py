"""
==============================================================================
TESTES AUTOMATIZADOS PARA O BFS
==============================================================================

Este arquivo contém testes para validar o funcionamento correto do algoritmo
BFS implementado. É útil para demonstrar a robustez da implementação.
==============================================================================
"""

from bfs_cidades import GrafoCidades, criar_mapa_brasil


def teste_caminho_existe():
    """
    Teste 1: Verificar se o BFS encontra caminhos que existem
    """
    print("\n" + "="*70)
    print("TESTE 1: Caminhos Existentes")
    print("="*70)
    
    mapa = criar_mapa_brasil()
    
    casos_teste = [
        ("São Paulo", "Rio de Janeiro", 1),
        ("Manaus", "Porto Alegre", 5),
        ("São Paulo", "Fortaleza", 4),
        ("Curitiba", "Brasília", 3),
    ]
    
    sucesso = 0
    total = len(casos_teste)
    
    for origem, destino, distancia_esperada in casos_teste:
        resultado = mapa.bfs_caminho_mais_curto(origem, destino)
        
        if resultado:
            caminho, distancia = resultado
            if distancia == distancia_esperada:
                print(f"✓ PASSOU: {origem} → {destino} (distância: {distancia})")
                sucesso += 1
            else:
                print(f"✗ FALHOU: {origem} → {destino}")
                print(f"  Esperado: {distancia_esperada}, Obtido: {distancia}")
        else:
            print(f"✗ FALHOU: {origem} → {destino} (caminho não encontrado)")
    
    print(f"\nResultado: {sucesso}/{total} testes passaram")
    return sucesso == total


def teste_mesma_cidade():
    """
    Teste 2: Verificar comportamento quando origem = destino
    """
    print("\n" + "="*70)
    print("TESTE 2: Origem = Destino")
    print("="*70)
    
    mapa = criar_mapa_brasil()
    resultado = mapa.bfs_caminho_mais_curto("São Paulo", "São Paulo")
    
    if resultado:
        caminho, distancia = resultado
        if len(caminho) == 1 and distancia == 0:
            print("✓ PASSOU: Origem = Destino tratado corretamente")
            return True
        else:
            print("✗ FALHOU: Origem = Destino não retornou distância 0")
            return False
    else:
        print("✗ FALHOU: Origem = Destino retornou None")
        return False


def teste_cidade_inexistente():
    """
    Teste 3: Verificar tratamento de cidades que não existem
    """
    print("\n" + "="*70)
    print("TESTE 3: Cidades Inexistentes")
    print("="*70)
    
    mapa = criar_mapa_brasil()
    
    casos = [
        ("Cidade Falsa", "São Paulo"),
        ("São Paulo", "Cidade Falsa"),
        ("Cidade Falsa 1", "Cidade Falsa 2"),
    ]
    
    sucesso = 0
    total = len(casos)
    
    for origem, destino in casos:
        resultado = mapa.bfs_caminho_mais_curto(origem, destino)
        
        if resultado is None:
            print(f"✓ PASSOU: {origem} → {destino} (tratado corretamente)")
            sucesso += 1
        else:
            print(f"✗ FALHOU: {origem} → {destino} (deveria retornar None)")
    
    print(f"\nResultado: {sucesso}/{total} testes passaram")
    return sucesso == total


def teste_caminho_minimo():
    """
    Teste 4: Verificar se o BFS realmente encontra o caminho MÍNIMO
    """
    print("\n" + "="*70)
    print("TESTE 4: Garantia de Caminho Mínimo")
    print("="*70)
    
    # Cria um grafo simples para teste
    mapa = GrafoCidades()
    
    # Grafo em forma de losango:
    #     A
    #    / \
    #   B   C
    #  / \ / \
    # D   E   F
    #      \ /
    #       G
    
    mapa.adicionar_estrada("A", "B")
    mapa.adicionar_estrada("A", "C")
    mapa.adicionar_estrada("B", "D")
    mapa.adicionar_estrada("B", "E")
    mapa.adicionar_estrada("C", "E")
    mapa.adicionar_estrada("C", "F")
    mapa.adicionar_estrada("E", "G")
    mapa.adicionar_estrada("F", "G")
    
    # O caminho mais curto de A para G deve ser: A → C → F → G (3 passos)
    # ou A → C → E → G (3 passos)
    # ou A → B → E → G (3 passos)
    
    resultado = mapa.bfs_caminho_mais_curto("A", "G")
    
    if resultado:
        caminho, distancia = resultado
        if distancia == 3:
            print(f"✓ PASSOU: Caminho mínimo encontrado (distância: {distancia})")
            print(f"  Caminho: {' → '.join(caminho)}")
            return True
        else:
            print(f"✗ FALHOU: Distância incorreta (esperado: 3, obtido: {distancia})")
            return False
    else:
        print("✗ FALHOU: Caminho não encontrado")
        return False


def teste_grafo_desconexo():
    """
    Teste 5: Verificar comportamento em grafo desconexo
    """
    print("\n" + "="*70)
    print("TESTE 5: Grafo Desconexo")
    print("="*70)
    
    # Cria um grafo com duas componentes separadas
    mapa = GrafoCidades()
    
    # Componente 1: A - B - C
    mapa.adicionar_estrada("A", "B")
    mapa.adicionar_estrada("B", "C")
    
    # Componente 2: X - Y - Z (separada da primeira)
    mapa.adicionar_estrada("X", "Y")
    mapa.adicionar_estrada("Y", "Z")
    
    # Tenta buscar caminho entre componentes diferentes
    resultado = mapa.bfs_caminho_mais_curto("A", "Z")
    
    if resultado is None:
        print("✓ PASSOU: Grafo desconexo tratado corretamente")
        return True
    else:
        print("✗ FALHOU: Encontrou caminho em grafo desconexo")
        return False


def teste_tamanho_grafo():
    """
    Teste 6: Verificar se o grafo tem o tamanho mínimo exigido
    """
    print("\n" + "="*70)
    print("TESTE 6: Tamanho do Grafo (Requisito: ≥ 16 vértices)")
    print("="*70)
    
    mapa = criar_mapa_brasil()
    num_vertices = len(mapa.grafo)
    num_arestas = sum(len(v) for v in mapa.grafo.values()) // 2
    
    print(f"Número de vértices: {num_vertices}")
    print(f"Número de arestas: {num_arestas}")
    
    if num_vertices >= 16:
        print(f"✓ PASSOU: Grafo tem {num_vertices} vértices (≥ 16)")
        return True
    else:
        print(f"✗ FALHOU: Grafo tem apenas {num_vertices} vértices (< 16)")
        return False


def teste_bidirecionalidade():
    """
    Teste 7: Verificar se as arestas são bidirecionais
    """
    print("\n" + "="*70)
    print("TESTE 7: Bidirecionalidade das Estradas")
    print("="*70)
    
    mapa = criar_mapa_brasil()
    
    # Testa alguns pares de cidades
    pares = [
        ("São Paulo", "Rio de Janeiro"),
        ("Brasília", "Salvador"),
        ("Curitiba", "Florianópolis"),
    ]
    
    sucesso = 0
    total = len(pares)
    
    for cidade1, cidade2 in pares:
        # Busca nos dois sentidos
        resultado1 = mapa.bfs_caminho_mais_curto(cidade1, cidade2)
        resultado2 = mapa.bfs_caminho_mais_curto(cidade2, cidade1)
        
        if resultado1 and resultado2:
            _, dist1 = resultado1
            _, dist2 = resultado2
            
            if dist1 == dist2:
                print(f"✓ PASSOU: {cidade1} ↔ {cidade2} (distância: {dist1})")
                sucesso += 1
            else:
                print(f"✗ FALHOU: {cidade1} ↔ {cidade2} (distâncias diferentes)")
        else:
            print(f"✗ FALHOU: {cidade1} ↔ {cidade2} (caminho não encontrado)")
    
    print(f"\nResultado: {sucesso}/{total} testes passaram")
    return sucesso == total


def executar_todos_testes():
    """
    Executa todos os testes e mostra um resumo
    """
    print("\n" + "="*70)
    print(" "*20 + "SUITE DE TESTES BFS")
    print("="*70)
    
    testes = [
        ("Caminhos Existentes", teste_caminho_existe),
        ("Origem = Destino", teste_mesma_cidade),
        ("Cidades Inexistentes", teste_cidade_inexistente),
        ("Caminho Mínimo", teste_caminho_minimo),
        ("Grafo Desconexo", teste_grafo_desconexo),
        ("Tamanho do Grafo", teste_tamanho_grafo),
        ("Bidirecionalidade", teste_bidirecionalidade),
    ]
    
    resultados = []
    
    for nome, funcao_teste in testes:
        try:
            passou = funcao_teste()
            resultados.append((nome, passou))
        except Exception as e:
            print(f"\n❌ ERRO no teste '{nome}': {str(e)}")
            resultados.append((nome, False))
    
    # Resumo final
    print("\n" + "="*70)
    print("RESUMO DOS TESTES")
    print("="*70)
    
    total = len(resultados)
    passou = sum(1 for _, p in resultados if p)
    
    for nome, passou_teste in resultados:
        status = "✓ PASSOU" if passou_teste else "✗ FALHOU"
        print(f"{status:10} | {nome}")
    
    print("="*70)
    print(f"Total: {passou}/{total} testes passaram ({passou*100//total}%)")
    print("="*70 + "\n")
    
    if passou == total:
        print("🎉 TODOS OS TESTES PASSARAM! Implementação correta.")
    else:
        print(f"⚠️  {total - passou} teste(s) falharam. Revise a implementação.")


if __name__ == "__main__":
    """
    Executa a suíte de testes quando o arquivo é executado diretamente
    """
    executar_todos_testes()
