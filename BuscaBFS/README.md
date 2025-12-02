# 🔍 Algoritmo BFS (Breadth-First Search)

## 📋 Informações do Projeto

**Disciplina:** Algoritmos em Grafos e Árvores  
**Tema:** Algoritmos de Busca e Caminhamento em Grafos  
**Algoritmo Implementado:** BFS (Busca em Largura)  
**Data:** Dezembro 2025

---

## 🎯 Problema Simulado

Este projeto implementa o algoritmo **BFS** para resolver o problema de **navegação entre cidades brasileiras**, encontrando o **caminho mais curto** (menor número de conexões) entre duas cidades.

### Cenário Real
Imagine um sistema de GPS que precisa encontrar a rota com menos trocas de estradas entre duas cidades. O BFS é perfeito para isso, pois garante encontrar o caminho com menos "saltos" (conexões).

---

## 🏗️ Estrutura do Grafo

### Características
- **Tipo:** Grafo não-direcionado (estradas de mão dupla)
- **Vértices:** 20 cidades brasileiras (requisito: mínimo de 16 ✓)
- **Arestas:** 28 conexões entre cidades
- **Representação:** Lista de adjacências

### Cidades Incluídas
```
Região Sudeste: São Paulo, Rio de Janeiro, Belo Horizonte, Campinas, Vitória
Região Sul: Curitiba, Florianópolis, Porto Alegre
Região Centro-Oeste: Brasília, Goiânia, Campo Grande, Cuiabá
Região Nordeste: Salvador, Recife, Fortaleza, Natal, Teresina, São Luís
Região Norte: Palmas, Belém, Manaus
```

---

## 🧠 Como o BFS Funciona

### Conceito Principal
O BFS explora o grafo **em camadas**, garantindo que sempre encontra o caminho mais curto em grafos não ponderados.

### Passo a Passo

1. **Inicialização**
   ```
   - Coloca a cidade de origem na fila
   - Marca a origem como visitada
   ```

2. **Exploração por Níveis**
   ```
   Nível 1: Vizinhos diretos da origem
   Nível 2: Vizinhos dos vizinhos
   Nível 3: E assim por diante...
   ```

3. **Processamento**
   ```
   Para cada cidade na fila:
   - Remove a cidade da fila (FIFO)
   - Verifica se é o destino
   - Se não, adiciona seus vizinhos não visitados à fila
   ```

4. **Garantia**
   - Por explorar em camadas, o BFS **sempre** encontra o caminho mais curto primeiro

### Complexidade
- **Temporal:** O(V + E) onde V = vértices e E = arestas
- **Espacial:** O(V) para armazenar a fila e visitados

---

## 💻 Estruturas de Dados Utilizadas

### 1. Dicionário (grafo)
```python
{
    "São Paulo": ["Rio de Janeiro", "Belo Horizonte", "Curitiba", "Campinas"],
    "Rio de Janeiro": ["São Paulo", "Belo Horizonte", "Vitória"],
    ...
}
```
- Representa as conexões entre cidades
- Acesso rápido aos vizinhos: O(1)

### 2. Deque (fila)
```python
fila = deque(["São Paulo"])
```
- Implementa a fila FIFO (First In, First Out)
- Operações eficientes: O(1) para adicionar e remover

### 3. Set (visitados)
```python
visitados = {"São Paulo", "Rio de Janeiro"}
```
- Evita processar a mesma cidade duas vezes
- Verificação rápida: O(1)

### 4. Dicionário (pais)
```python
pais = {
    "Rio de Janeiro": "São Paulo",
    "Belo Horizonte": "São Paulo"
}
```
- Rastreia de onde viemos
- Permite reconstruir o caminho ao final

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado
- Nenhuma biblioteca externa necessária (usa apenas biblioteca padrão)

### Passo 1: Verificar Python
```bash
python --version
```

### Passo 2: Executar o Programa
```bash
python bfs_cidades.py
```

### Passo 3: Usar o Menu
O programa oferece um menu interativo com opções:
1. Buscar caminho entre duas cidades (entrada manual)
2. Ver o mapa completo de conexões
3. Executar exemplos pré-definidos
4. Sair

---

## 📊 Exemplos de Execução

### Exemplo 1: Manaus → Porto Alegre
```
Entrada: origem = "Manaus", destino = "Porto Alegre"

Resultado:
✓ Caminho encontrado!
📏 Distância: 5 conexões
🗺️ Caminho:
   🚗 Manaus (INÍCIO)
   1. Palmas
   2. Brasília
   3. São Paulo
   4. Curitiba
   🎯 Porto Alegre (FIM)
```

### Exemplo 2: São Paulo → Fortaleza
```
Entrada: origem = "São Paulo", destino = "Fortaleza"

Resultado:
✓ Caminho encontrado!
📏 Distância: 3 conexões
🗺️ Caminho:
   🚗 São Paulo (INÍCIO)
   1. Belo Horizonte
   2. Brasília
   3. Salvador
   🎯 Fortaleza (FIM)
```

### Exemplo 3: Rio de Janeiro → Cuiabá
```
Entrada: origem = "Rio de Janeiro", destino = "Cuiabá"

Resultado:
✓ Caminho encontrado!
📏 Distância: 4 conexões
🗨️ Caminho:
   🚗 Rio de Janeiro (INÍCIO)
   1. São Paulo
   2. Campo Grande
   🎯 Cuiabá (FIM)
```

---

## 📝 Código Comentado

O código está **extensivamente comentado** com:

### ✅ Comentários de Cabeçalho
- Explicação geral do projeto
- Problema simulado
- Informações da equipe

### ✅ Docstrings
- Todas as classes têm docstrings explicativas
- Todos os métodos documentam parâmetros e retornos
- Exemplos de uso quando relevante

### ✅ Comentários Inline
- Cada seção do algoritmo BFS explicada
- Justificativas para escolhas de estruturas de dados
- Explicação de casos especiais

### ✅ Visualização do Fluxo
- Prints detalhados durante a execução do BFS
- Mostra cada nível sendo explorado
- Exibe cidades visitadas e vizinhos adicionados

---

## 🎓 Conceitos Importantes para a Apresentação

### 1. Por que BFS?
- Garante encontrar o **caminho mais curto** em grafos não ponderados
- Explora de forma **sistemática** e **completa**
- Ideal para problemas de **menor distância em saltos**

### 2. Diferença: BFS vs DFS
| Característica | BFS | DFS |
|----------------|-----|-----|
| Estrutura | Fila (FIFO) | Pilha (LIFO) |
| Exploração | Por níveis | Por profundidade |
| Caminho | Mais curto | Não garante |
| Memória | Mais memória | Menos memória |

### 3. Aplicações Reais do BFS
- 🗺️ GPS e sistemas de navegação
- 🌐 Crawlers de web
- 🔌 Análise de redes sociais (amigos próximos)
- 🎮 IA de jogos (movimento de personagens)
- 📱 Roteamento em redes de computadores

### 4. Vantagens da Implementação
- ✓ Código limpo e organizado (OOP)
- ✓ Comentários detalhados para entendimento
- ✓ Interface interativa (fácil demonstração)
- ✓ Visualização do processo passo a passo
- ✓ Exemplos prontos para apresentação

---

## 📂 Estrutura de Arquivos

```
GrafosBusca/
│
├── bfs_cidades.py          # Código principal do BFS
└── README.md               # Esta documentação
```

---

## 🎬 Roteiro para Apresentação em Vídeo

### 1. Introdução (1-2 min)
- Apresentar o problema: navegação entre cidades
- Explicar por que escolhemos BFS
- Mostrar o grafo visualmente (desenhar ou usar imagem)

### 2. Teoria do BFS (2-3 min)
- Explicar o conceito de busca em largura
- Mostrar como funciona em camadas
- Usar um exemplo pequeno no quadro (4-5 vértices)

### 3. Estruturas de Dados (2 min)
- Explicar cada estrutura usada (fila, set, dict)
- Justificar as escolhas
- Mostrar como funcionam juntas

### 4. Demonstração do Código (4-5 min)
- Abrir o código e explicar a classe GrafoCidades
- Detalhar a função bfs_caminho_mais_curto
- Mostrar os comentários e explicações

### 5. Execução Prática (3-4 min)
- Executar o programa
- Mostrar o mapa de 20 cidades
- Executar 2-3 buscas diferentes
- Explicar a saída passo a passo

### 6. Análise de Complexidade (1 min)
- Explicar O(V + E)
- Mencionar a garantia de caminho mínimo

### 7. Conclusão (1 min)
- Recapitular pontos principais
- Aplicações reais
- Perguntas

**Tempo Total:** 15-18 minutos

---

## 🔧 Possíveis Extensões

Se quiser impressionar ainda mais, você pode adicionar:

1. **Visualização Gráfica**
   - Usar networkx e matplotlib para desenhar o grafo
   - Destacar o caminho encontrado em cores

2. **Pesos nas Arestas**
   - Adicionar distâncias em km
   - Comparar BFS (menos conexões) vs Dijkstra (menor km)

3. **Estatísticas**
   - Número de cidades visitadas
   - Tempo de execução
   - Comparação de diferentes caminhos

4. **Interface Gráfica**
   - Criar uma GUI com tkinter
   - Permitir clicar nas cidades

---

## 📚 Referências

- Cormen, T. H. et al. *Introduction to Algorithms* (CLRS)
- Sedgewick, R. *Algorithms in Python*
- Material de aula sobre Grafos

---

## ✅ Checklist de Requisitos

- [x] Implementação do algoritmo BFS
- [x] Problema específico (navegação entre cidades)
- [x] Código fonte comentado detalhadamente
- [x] Grafo com mínimo de 16 vértices (20 cidades)
- [x] Explicação completa do funcionamento
- [x] Interface para demonstração
- [x] Documentação completa (README)

---

## 👥 Informações da Equipe

**Membros:**
- [Seu nome aqui]
- [Adicione os membros da sua equipe]

**Linguagem:** Python 3.x  
**Data de Entrega:** [Data aqui]

---

## 📧 Contato

Para dúvidas sobre a implementação, entre em contato com a equipe.

---

**Boa apresentação! 🎯**
