# DFS - Algoritmo de Busca em Profundidade
## Mapeamento de Cidades Brasileiras

## 📋 Descrição

Este projeto implementa o algoritmo **DFS (Depth-First Search)** aplicado ao problema de mapeamento e exploração de rotas entre cidades brasileiras. O DFS é um algoritmo fundamental em teoria dos grafos que explora o grafo indo o mais profundo possível em cada ramo antes de retroceder.

## 🎯 Objetivos

- ✅ Implementar DFS recursivo e iterativo
- ✅ Usar grafo com mais de 16 vértices (cidades)
- ✅ Simular problema real: rotas entre cidades brasileiras
- ✅ Visualizar o grafo e o caminho percorrido
- ✅ Código detalhadamente comentado
- ✅ Incluir testes unitários

## 🗺️ O Problema

O programa simula um sistema de rotas de transporte entre as principais cidades do Brasil, cobrindo todas as 5 regiões:

- **Sudeste**: São Paulo, Rio de Janeiro, Belo Horizonte, Campinas, Vitória, Ribeirão Preto
- **Sul**: Curitiba, Porto Alegre, Florianópolis
- **Centro-Oeste**: Brasília, Goiânia, Campo Grande, Cuiabá
- **Nordeste**: Salvador, Recife, Fortaleza, Natal, Aracaju
- **Norte**: Manaus, Belém, Porto Velho, São Luís

**Total: 25 cidades (vértices)** ✅ Mais que os 16 vértices obrigatórios

## 🔍 Como Funciona o DFS

### Conceito

O DFS (Depth-First Search) é um algoritmo de busca que:

1. Começa em um vértice inicial
2. Explora o máximo possível ao longo de cada ramo antes de retroceder
3. Usa uma estrutura de **pilha** (explícita ou através de recursão)
4. Marca vértices como visitados para evitar loops infinitos

### Pseudocódigo

```
DFS(vertice_atual, visitados):
    marcar vertice_atual como visitado
    
    para cada vizinho de vertice_atual:
        se vizinho não foi visitado:
            DFS(vizinho, visitados)
```

### Complexidade

- **Tempo**: O(V + E) - onde V = vértices e E = arestas
- **Espaço**: O(V) - para armazenar vértices visitados

## 📁 Arquivos

- `dfs_cidades_brasil.py` - Implementação completa do DFS
- `testes_dfs.py` - Testes unitários
- `README.md` - Esta documentação

## 🚀 Como Executar

### Requisitos

```bash
pip install matplotlib networkx
```

### Execução Principal

```bash
python dfs_cidades_brasil.py
```

### Executar Testes

```bash
python testes_dfs.py
```

## 📊 Funcionalidades Implementadas

### 1. DFS Recursivo
```python
caminho = grafo.dfs_recursivo("São Paulo")
```
Implementação usando recursão, mais elegante e intuitiva.

### 2. DFS Iterativo
```python
caminho = grafo.dfs_iterativo("São Paulo")
```
Implementação usando pilha explícita, evita estouro de pilha.

### 3. Encontrar Caminho entre Cidades
```python
caminho = grafo.encontrar_caminho_dfs("São Paulo", "Manaus")
```
Usa DFS para encontrar um caminho entre duas cidades.

### 4. DFS Completo (Componentes Conectados)
```python
componentes = grafo.dfs_completo()
```
Identifica todos os componentes conectados do grafo.

### 5. Detecção de Ciclos
```python
tem_ciclo = grafo.detectar_ciclo()
```
Verifica se o grafo possui ciclos.

### 6. Visualização do Grafo
```python
grafo.visualizar_grafo("Título", caminho_destaque)
```
Gera visualização gráfica com matplotlib/networkx.

## 📈 Exemplo de Saída

```
==============================================================
ALGORITMO DFS - BUSCA EM PROFUNDIDADE
Aplicação: Exploração de Cidades Brasileiras
==============================================================

==============================================================
ESTATÍSTICAS DO GRAFO
==============================================================
Número de cidades (vértices): 25
Número de conexões (arestas): 28
Grau médio: 2.24
Cidade com mais conexões: São Paulo (4 conexões)
Possui ciclos: Sim
==============================================================

==============================================================
DEMONSTRAÇÃO 1: DFS RECURSIVO
==============================================================

Iniciando busca a partir de: São Paulo

Visitando: São Paulo
Visitando: Rio de Janeiro
Visitando: Belo Horizonte
Visitando: Vitória
Visitando: Brasília
...

Ordem de visitação: São Paulo -> Rio de Janeiro -> Belo Horizonte -> ...
Total de cidades visitadas: 25
```

## 🎓 Conceitos Importantes

### Aplicações do DFS

1. **Detecção de Ciclos** - Identificar loops no grafo
2. **Ordenação Topológica** - Para grafos direcionados acíclicos
3. **Componentes Fortemente Conectados** - Identificar subgrafos
4. **Resolução de Labirintos** - Encontrar caminhos
5. **Análise de Conectividade** - Verificar se o grafo é conexo

### Diferenças DFS vs BFS

| Característica | DFS | BFS |
|----------------|-----|-----|
| Estrutura de Dados | Pilha | Fila |
| Exploração | Profundidade primeiro | Largura primeiro |
| Caminho Encontrado | Qualquer caminho | Caminho mais curto |
| Memória | Menor (altura) | Maior (largura) |
| Uso Recursivo | Natural | Menos natural |

## 📝 Notas para Apresentação

### Pontos a Destacar

1. **Grafo Real**: Uso de cidades brasileiras torna o problema tangível
2. **Duas Implementações**: Recursiva e iterativa demonstram versatilidade
3. **Visualização**: Gráficos facilitam compreensão
4. **Testes**: Garantem corretude da implementação
5. **Documentação**: Código totalmente comentado

### Demonstrações Sugeridas

1. Executar DFS a partir de diferentes cidades
2. Mostrar diferença entre DFS recursivo e iterativo
3. Encontrar caminho entre cidades específicas
4. Mostrar visualização do grafo
5. Executar testes unitários

## 🔧 Possíveis Extensões

- [ ] Adicionar pesos nas arestas (distâncias reais)
- [ ] Implementar DFS limitado por profundidade
- [ ] Adicionar mais métricas e estatísticas
- [ ] Criar interface gráfica interativa
- [ ] Comparar performance com BFS

## 👥 Informações do Projeto

**Disciplina**: Teoria dos Grafos  
**Algoritmo**: DFS (Depth-First Search)  
**Problema**: Mapeamento de Cidades Brasileiras  
**Linguagem**: Python 3.x

---

## 📚 Referências

- Cormen, T. H., et al. "Introduction to Algorithms" (CLRS)
- Sedgewick, R. "Algorithms, 4th Edition"
- NetworkX Documentation: https://networkx.org/
- Matplotlib Documentation: https://matplotlib.org/

---

**Última atualização**: Dezembro 2025
