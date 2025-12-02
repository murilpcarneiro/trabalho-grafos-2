# 🎬 Guia para Apresentação em Vídeo - DFS

## ⏱️ Estrutura da Apresentação (5 minutos para DFS)

### 1. Introdução (30 segundos)

**O que falar:**
- "Vamos apresentar o algoritmo DFS (Depth-First Search) aplicado ao mapeamento de cidades brasileiras"
- "O DFS é um algoritmo fundamental de busca em grafos que explora em profundidade"

### 2. Conceito do DFS (1 minuto)

**O que explicar:**

```
🌳 DFS - Depth First Search (Busca em Profundidade)

Princípio: Vai o mais fundo possível antes de retroceder

Analogia: Como explorar um labirinto sempre seguindo 
          pela esquerda até bater em beco sem saída

Estrutura: Usa PILHA (Stack)
- Recursão: pilha implícita
- Iterativo: pilha explícita
```

**Mostrar no quadro/slide:**
```
Exemplo simples:
    A
   / \
  B   C
 / \
D   E

DFS a partir de A: A → B → D → E → C
(vai fundo primeiro: A→B→D, depois volta e continua)
```

### 3. Complexidade (30 segundos)

**O que explicar:**
- **Tempo**: O(V + E) - Visita cada vértice uma vez e explora cada aresta
- **Espaço**: O(V) - Armazena vértices visitados
- V = vértices, E = arestas

### 4. O Problema Resolvido (45 segundos)

**Mostrar na tela:**
```python
# Mostrando o código da criação do grafo
def criar_grafo_brasil():
    # 25 cidades brasileiras (>16 vértices ✅)
    # 5 regiões do Brasil
```

**Explicar:**
- "Criamos um grafo com 25 cidades do Brasil"
- "Representa rotas de transporte entre cidades"
- "Cobre todas as 5 regiões: Norte, Nordeste, Centro-Oeste, Sudeste e Sul"

### 5. Demonstração do Código (2 minutos)

#### 5.1 Mostrar Implementação Recursiva (45s)

```python
def dfs_recursivo(self, cidade_inicial, visitados=None, caminho=None):
    # Marcar como visitada
    visitados.add(cidade_inicial)
    caminho.append(cidade_inicial)
    
    # Explorar vizinhos não visitados
    for vizinho in self.grafo[cidade_inicial]:
        if vizinho not in visitados:
            self.dfs_recursivo(vizinho, visitados, caminho)
```

**Explicar:**
1. Marca cidade atual como visitada
2. Para cada vizinho não visitado, chama recursivamente
3. A recursão cria a pilha implícita

#### 5.2 Executar o Programa (45s)

**No terminal:**
```bash
python dfs_cidades_brasil.py
```

**Mostrar:**
- Estatísticas do grafo (25 vértices, 28 arestas)
- Execução do DFS recursivo saindo de São Paulo
- Ordem de visitação
- Visualização gráfica

#### 5.3 Mostrar Funcionalidades Extras (30s)

**Demonstrar rapidamente:**
```python
# 1. Encontrar caminho
caminho = grafo.encontrar_caminho_dfs("São Paulo", "Manaus")
# Output: São Paulo → Brasília → Manaus

# 2. Detectar ciclos
tem_ciclo = grafo.detectar_ciclo()
# Output: Sim (grafo tem ciclos)
```

### 6. Conclusão (30 segundos)

**Resumir:**
- ✅ DFS implementado (recursivo e iterativo)
- ✅ Mais de 16 vértices (25 cidades)
- ✅ Problema real (rotas entre cidades)
- ✅ Visualização gráfica
- ✅ Código totalmente comentado

---

## 🎯 Pontos Importantes a Mencionar

### Durante a Apresentação

1. **Originalidade**: "Implementação própria, não copiada"
2. **Completude**: "Código totalmente documentado com comentários"
3. **Testes**: "Incluímos testes unitários para validação"
4. **Requisitos**: "Atende todos os requisitos: >16 vértices, problema específico, visualização"

### Diferencial do Nosso Trabalho

- 📊 **Visualização gráfica** do caminho percorrido
- 🧪 **Testes unitários** completos
- 📚 **Documentação detalhada**
- 🔄 **Duas implementações**: recursiva e iterativa
- 🗺️ **Problema real e brasileiro**

---

## 💡 Dicas para a Gravação

### Preparação

1. **Teste antes**: Execute o código antes de gravar
2. **Feche outras janelas**: Mantenha apenas o necessário aberto
3. **Zoom**: Aumente o tamanho da fonte do editor/terminal
4. **Internet**: Verifique se matplotlib está instalado

### Durante a Gravação

1. **Fale claramente**: Não corra ao falar
2. **Pause após conceitos**: Dê tempo para absorção
3. **Aponte na tela**: Use cursor para destacar partes importantes
4. **Mostre resultados**: Deixe visualizações visíveis por alguns segundos

### Estrutura do Vídeo

```
00:00 - 00:30  │ Introdução
00:30 - 01:30  │ Explicação do DFS (conceito)
01:30 - 02:15  │ Apresentação do problema
02:15 - 04:00  │ Demonstração do código rodando
04:00 - 04:30  │ Funcionalidades extras
04:30 - 05:00  │ Conclusão
```

---

## 📋 Checklist Pré-Gravação

- [ ] Código está funcionando sem erros
- [ ] Matplotlib e NetworkX instalados
- [ ] Terminal com fonte legível
- [ ] Editor com zoom adequado
- [ ] Exemplos preparados
- [ ] Gráficos sendo gerados corretamente
- [ ] Microfone testado
- [ ] Ambiente silencioso

---

## 🎤 Script Sugerido

### Abertura

> "Olá, vamos apresentar nossa implementação do algoritmo DFS, Depth-First Search ou Busca em Profundidade. Aplicamos o algoritmo ao problema de mapeamento de cidades brasileiras."

### Explicando DFS

> "O DFS é um algoritmo que explora grafos em profundidade. Imagine que você está em um labirinto: o DFS seria como escolher um caminho e ir até o fim dele antes de voltar e tentar outro caminho. Diferente do BFS que explora por níveis, o DFS usa uma pilha e vai o mais fundo possível primeiro."

### Mostrando o Código

> "Aqui está nossa implementação recursiva do DFS. O algoritmo recebe uma cidade inicial, marca ela como visitada, e então para cada vizinho não visitado, chama recursivamente o DFS. A complexidade é O(V+E), linear no tamanho do grafo."

### Executando

> "Vamos executar o programa. Como podem ver, nosso grafo tem 25 cidades brasileiras, cobrindo todas as 5 regiões do país. Iniciando a busca a partir de São Paulo..."

### Finalizando

> "Como demonstramos, nossa implementação atende todos os requisitos: mais de 16 vértices, resolve um problema específico, o código está totalmente comentado, e incluímos visualização gráfica e testes unitários."

---

## 📊 Elementos Visuais para Mostrar

1. **Grafo completo** - visualização inicial
2. **Caminho DFS destacado** - em vermelho
3. **Output do terminal** - ordem de visitação
4. **Código comentado** - destacar comentários
5. **Testes passando** - mostrar sucesso dos testes

---

## ⚠️ Erros Comuns a Evitar

1. ❌ Não explicar apenas o código - explique o conceito primeiro
2. ❌ Não falar muito rápido - deixe tempo para compreensão
3. ❌ Não esquecer de mostrar que tem >16 vértices
4. ❌ Não pular a parte de complexidade
5. ❌ Não esquecer de mencionar que o código é original

---

**Boa apresentação! 🚀**
