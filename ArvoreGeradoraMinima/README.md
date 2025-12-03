# 🌳 Algoritmos de Árvore Geradora Mínima (MST)

## 📋 Informações do Projeto

**Disciplina:** Algoritmos em Grafos e Árvores
**Tema:** Árvores Geradoras Mínimas
**Algoritmos Implementados:** Kruskal e Prim
**Data:** Dezembro 2025

---

## 🎯 Problema Simulado

Este projeto implementa algoritmos de **Árvore Geradora Mínima (MST)** para resolver o problema de **otimização de infraestrutura de estradas**, conectando todas as cidades com o **menor custo total de construção**.

### Cenário Real

Imagine uma empresa de construção que precisa conectar 20 cidades com estradas. O objetivo é minimizar o custo/distância total enquanto garante que todas as cidades fiquem conectadas. Uma MST resolve exatamente isso!

---

## 🏗️ Estrutura do Grafo

### Características

- **Tipo:** Grafo não-direcionado ponderado
- **Vértices:** 20 cidades brasileiras (requisito: mínimo de 16 ✓)
- **Arestas:** 28 conexões com pesos (distâncias em km)
- **Representação:** Lista de adjacências e lista de arestas

### Cidades Incluídas

```
Região Sudeste: São Paulo, Rio de Janeiro, Belo Horizonte, Campinas, Vitória
Região Sul: Curitiba, Florianópolis, Porto Alegre
Região Centro-Oeste: Brasília, Goiânia, Campo Grande, Cuiabá
Região Nordeste: Salvador, Recife, Fortaleza, Natal, Teresina, São Luís
Região Norte: Palmas, Belém, Manaus
```

---

## 🧠 Como as MSTs Funcionam

### Conceito Principal

Uma **Árvore Geradora Mínima** é um subconjunto de arestas que:

- ✓ Conecta todos os vértices
- ✓ Não contém ciclos
- ✓ Tem peso total **mínimo** possível

### Propriedade Importante

Para um grafo com V vértices, uma MST sempre tem exatamente **V-1 arestas**.

### Exemplo Visual

```
Grafo com 5 cidades:
    A --- 5 --- B
    |           |
    3           4
    |           |
    C --- 2 --- D
         / \
        1   1
       /     \
      E       (não incluímos)

MST = {AC(3), CD(2), CE(1), DB(4)} = peso total 10
```

---

## 🔍 Algoritmo de Kruskal

### Funcionamento Passo a Passo

1. **Ordenação**

   ```
   Ordena TODAS as arestas por peso (crescente)
   ```

2. **Seleção Gulosa**

   ```
   Para cada aresta (em ordem de peso):
   - Se adicionar esta aresta NÃO criar um ciclo
   - Adiciona à MST
   - Senão, descarta
   ```

3. **Parada**
   ```
   Continua até ter V-1 arestas
   ```

### Estrutura de Dados: Union-Find

O **Union-Find** (também chamado Disjoint Set Union) detecta ciclos eficientemente:

```python
# Inicializa: cada vértice é seu próprio conjunto
{A}, {B}, {C}, {D}, {E}

# Adiciona aresta A-C:
{A, C}, {B}, {D}, {E}

# Adiciona aresta C-D:
{A, C, D}, {B}, {E}

# Tenta adicionar A-D:
⚠️ A e D já estão no mesmo conjunto → criaria ciclo!
```

### Complexidade

- **Temporal:** O(E log E) - dominado pela ordenação
- **Espacial:** O(V + E)

### Características

- ✓ Funciona com grafos desconexos (cria floresta)
- ✓ Excelente para grafos esparsos
- ✓ Ordem de processamento é determinística

---

## 🌲 Algoritmo de Prim

### Funcionamento Passo a Passo

1. **Inicialização**

   ```
   Começa com um vértice arbitrário
   Coloca ele na árvore (MST)
   ```

2. **Crescimento Incremental**

   ```
   Repete até ter V-1 arestas:
   - Encontra a MENOR aresta que conecta
     um vértice NA árvore a um vértice FORA
   - Adiciona essa aresta e o vértice à árvore
   ```

3. **Visualização**
   ```
   Começa:  {A}
   Adiciona AC(3):  {A, C}
   Adiciona CE(1):  {A, C, E}
   Adiciona CD(2):  {A, C, E, D}
   Adiciona DB(4):  {A, C, E, D, B}
   ```

### Complexidade

- **Temporal:** O(V²) com implementação simples (heap: O(E log V))
- **Espacial:** O(V)

### Características

- ✓ Excelente para grafos densos
- ✓ Cresce como uma árvore a partir de um vértice
- ✓ Pode começar de qualquer vértice (resultado é o mesmo)

---

## 📊 Diferença: Kruskal vs Prim

| Aspecto               | Kruskal         | Prim             |
| --------------------- | --------------- | ---------------- |
| **Abordagem**         | Ordena arestas  | Cresce árvore    |
| **Começam**           | Sem restrição   | De um vértice    |
| **Melhor Para**       | Grafos esparsos | Grafos densos    |
| **Estrutura**         | Union-Find      | Set de visitados |
| **Complexidade**      | O(E log E)      | O(V²)            |
| **MST Encontrada**    | Mesma MST       | Mesma MST        |
| **Ordem das Arestas** | Diferente       | Diferente        |

### ⚠️ Importante

**Ambos encontram a MESMA MST** com o **MESMO peso total**! A diferença está na ordem em que as arestas são adicionadas.

---

## 💻 Estruturas de Dados

### 1. Classe Aresta

```python
@dataclass
class Aresta:
    origem: str      # Primeira cidade
    destino: str     # Segunda cidade
    peso: float      # Distância/custo
```

### 2. Classe UnionFind

```python
class UnionFind:
    pai: Dict[str, str]  # Representante de cada elemento
    rank: Dict[str, int] # Rank para otimização

    find(x)      # O(α(n)) - encontra representante
    union(x, y)  # O(α(n)) - une conjuntos
    sao_conectados(x, y)  # Verifica se x e y conectados
```

### 3. Classe GrafoMST

```python
class GrafoMST:
    arestas: List[Aresta]              # Todas as arestas
    adjacencias: Dict[str, List]        # Lista de adjacências ponderada
    cidades: Set[str]                   # Todos os vértices
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa necessária

### Passo 1: Verificar Python

```bash
python --version
```

### Passo 2: Executar o Programa

```bash
python mst_cidades.py
```

### Passo 3: Usar o Menu

O programa oferece opções para:

1. Executar algoritmo de Kruskal
2. Executar algoritmo de Prim
3. Comparar os dois algoritmos
4. Ver o mapa novamente
5. Sair

---

## 📊 Exemplos de Execução

### Exemplo 1: Kruskal

```
ALGORITMO DE KRUSKAL
───────────────────────
✓ ADICIONA: São Paulo ↔ Campinas (99 km) - MST agora tem 1 arestas
✓ ADICIONA: Brasília ↔ Goiânia (209 km) - MST agora tem 2 arestas
✓ ADICIONA: Brasília ↔ Palmas (897 km) - MST agora tem 3 arestas
...

RESULTADO - ÁRVORE GERADORA MÍNIMA (Kruskal)
═════════════════════════════════════════════
✓ Estradas necessárias para conectar todas as cidades:

  1. São Paulo           ↔ Campinas                   |    99.0 km
  2. Brasília            ↔ Goiânia                    |   209.0 km
  3. Florianópolis       ↔ Porto Alegre               |   473.0 km
  ...

RESUMO DA MST:
   Total de estradas: 19
   Distância total: 10,847 km
   Se construísse todas: 15,326 km
   Economia: 4,479 km (29.2%)
```

### Exemplo 2: Prim

```
ALGORITMO DE PRIM
─────────────────
🌳 Iniciando a partir de: São Paulo

🎯 Etapa 1: Vértices na MST = 1, Fora = 19

🎯 Etapa 2: ADICIONA
   Aresta: São Paulo ↔ Campinas (99 km)
   Vértices na MST: 2, Fora: 18
   Peso total acumulado: 99 km

🎯 Etapa 3: ADICIONA
   Aresta: São Paulo ↔ Rio de Janeiro (430 km)
   ...

✓ MST COMPLETA com 19 arestas!
```

---

## 🎓 Conceitos Importantes

### 1. Por que MST é Importante?

Real-world applications:

- 🌐 Redes de telecomunicações (fibra óptica)
- 🏗️ Infraestrutura de estradas
- 💡 Distribuição de energia elétrica
- 🚇 Planejamento de transporte público
- 🖥️ Redes de computadores

### 2. Propriedade do Corte (Cut Property)

Para qualquer corte (partição) do grafo:

> "A aresta de menor peso que atravessa o corte está em alguma MST"

Isso justifica ambos os algoritmos!

### 3. Propriedade do Ciclo (Cycle Property)

> "Em qualquer ciclo do grafo, a aresta de maior peso NÃO está em nenhuma MST"

### 4. Unicidade

- Se todos os pesos forem distintos → MST é **única**
- Se houver empates → pode haver múltiplas MSTs com o mesmo peso

---

## 📂 Estrutura de Arquivos

```
ArvoreGeradoraMinima/
│
├── mst_cidades.py          # Código principal (Kruskal + Prim)
├── README.md               # Esta documentação
├── RESUMO_EXECUTIVO.md     # Resumo dos algoritmos
├── GUIA_RAPIDO.md          # Guia rápido de uso
└── testes_mst.py           # Testes automatizados (opcional)
```

---

## 🔧 Código Comentado

O código inclui:

### ✅ Documentação Completa

- Docstrings para classes e métodos
- Explicação de cada algoritmo
- Exemplos de uso

### ✅ Comentários Detalhados

- Seções claramente marcadas
- Explicação de cada etapa
- Justificativas de decisões

### ✅ Visualização do Processo

- Prints detalhados durante execução
- Mostra cada aresta sendo processada
- Exibe progresso passo a passo

---

## 🎬 Roteiro para Apresentação

### 1. Introdução (1-2 min)

- Explicar o problema de otimização
- Mostrar o cenário real (construção de estradas)
- Definir MST formalmente

### 2. Teoria (2-3 min)

- Explicar conceitos fundamentais
- Mostrar exemplo visual no quadro
- Discutir propriedades (cut, cycle)

### 3. Kruskal (3 min)

- Explicar o algoritmo passo a passo
- Detalhar Union-Find
- Mostrar complexidade O(E log E)

### 4. Prim (3 min)

- Explicar o crescimento da árvore
- Comparar com Kruskal
- Mostrar complexidade O(V²)

### 5. Demonstração (4-5 min)

- Executar ambos os algoritmos
- Mostrar que encontram a mesma MST
- Comparar resultados

### 6. Aplicações (2 min)

- Exemplos reais
- Por que MST é importante
- Extensões possíveis

**Tempo Total:** 15-18 minutos

---

## 🔬 Análise de Complexidade

### Kruskal

```
Ordenação de arestas:        O(E log E)
E iterações:                 O(E)
Cada find/union:             O(α(V)) ≈ O(1)

Total:                       O(E log E)
Espaço:                      O(V + E)
```

### Prim (versão simples)

```
V iterações externas:        O(V)
Em cada iteração:            O(V + E) no pior caso
  - Buscar menor aresta:     O(E)
  - Atualizar structs:       O(V)

Total:                       O(V²) ou O(V(V+E))
Espaço:                      O(V)
```

### Prim (com heap)

```
V iterações com heap:        O(V)
E operações de extração:     O(E log V)

Total:                       O(E log V)
Espaço:                      O(V)
```

---

## ✅ Checklist de Requisitos

- [x] Implementação dos algoritmos Kruskal e Prim
- [x] Problema específico (otimização de estradas)
- [x] Código fonte comentado detalhadamente
- [x] Grafo com mínimo de 16 vértices (20 cidades)
- [x] Estruturas de dados apropriadas
- [x] Comparação entre os algoritmos
- [x] Explicação completa e clara
- [x] Interface interativa
- [x] Documentação completa

---

## 📚 Referências

- Cormen, T. H. et al. _Introduction to Algorithms_ (CLRS)
- Sedgewick, R. _Algorithms in Python_
- Material de aula sobre Grafos
- [Visualgo - Visualização de MST](https://visualgo.net/en/mst)

---

## 🔗 Relacionados

Verifique também a implementação de:

- BFS em `../BuscaBFS/bfs_cidades.py`
- Bellman-Ford em `../Bellman-Ford.py`

---

**Boa apresentação! 🎯**
