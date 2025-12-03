# 📚 Trabalho de Grafos - Algoritmos em Grafos e Árvores

## 🎯 Visão Geral

Este repositório contém implementações de algoritmos clássicos de grafos, seguindo um padrão profissional de documentação e código estruturado.

---

## 📂 Estrutura do Repositório

```
trabalho-grafos-2/
│
├── BuscaBFS/
│   ├── bfs_cidades.py           # Implementação do BFS
│   ├── README.md                # Documentação BFS
│   ├── RESUMO_EXECUTIVO.md      # Resumo BFS
│   ├── GUIA_RAPIDO.md           # Quick start BFS
│   ├── EXEMPLOS_VISUAIS.md      # Exemplos BFS
│   ├── testes_bfs.py            # Testes BFS
│   └── ...
│
├── ArvoreGeradoraMinima/
│   ├── mst_cidades.py           # Implementação MST (Kruskal + Prim)
│   ├── README.md                # Documentação MST
│   ├── RESUMO_EXECUTIVO.md      # Resumo MST
│   ├── GUIA_RAPIDO.md           # Quick start MST
│   ├── EXEMPLOS_VISUAIS.md      # Exemplos MST
│   ├── STATUS.md                # Status da implementação
│   ├── testes_mst.py            # Testes MST
│   └── teste_rapido.py          # Teste rápido
│
├── Bellman-Ford.py              # Algoritmo de Bellman-Ford
│
└── README.md                    # Este arquivo
```

---

## 🔍 Algoritmos Implementados

### 1. BFS (Breadth-First Search)

**Localização:** `BuscaBFS/`

**Problema:** Encontrar o caminho mais curto entre duas cidades brasileiras

**Características:**

- ✓ 20 cidades brasileiras
- ✓ Busca em largura
- ✓ Garantia de caminho mínimo
- ✓ Interface interativa
- ✓ Documentação completa

**Como usar:**

```bash
cd BuscaBFS
python bfs_cidades.py
```

---

### 2. MST - Árvores Geradoras Mínimas ⭐ NOVO

**Localização:** `ArvoreGeradoraMinima/`

**Problema:** Conectar todas as cidades com o menor custo total

**Algoritmos:**

1. **Kruskal** - Abordagem gulosa com ordenação

   - Complexidade: O(E log E)
   - Melhor para grafos esparsos

2. **Prim** - Crescimento incremental
   - Complexidade: O(V²)
   - Melhor para grafos densos

**Características:**

- ✓ 20-21 cidades brasileiras
- ✓ Dois algoritmos diferentes
- ✓ Comparação e validação
- ✓ UnionFind otimizado
- ✓ Análise de economia real (39% em Brasil)
- ✓ 1900+ linhas de documentação

**Como usar:**

```bash
cd ArvoreGeradoraMinima
python mst_cidades.py
```

---

### 3. Bellman-Ford

**Localização:** `Bellman-Ford.py`

Algoritmo para caminhos mais curtos com pesos negativos

---

## 📊 Comparação dos Algoritmos

| Algoritmo    | Tipo    | Complexidade | Ideal Para      |
| ------------ | ------- | ------------ | --------------- |
| BFS          | Busca   | O(V+E)       | Sem pesos       |
| Kruskal      | MST     | O(E log E)   | Esparso         |
| Prim         | MST     | O(V²)        | Denso           |
| Bellman-Ford | Caminho | O(VE)        | Pesos negativos |

---

## 🚀 Como Começar

### 1. Explorar BFS

```bash
cd BuscaBFS
python bfs_cidades.py
```

### 2. Explorar MST ⭐

```bash
cd ArvoreGeradoraMinima
python mst_cidades.py
```

### 3. Teste Rápido

```bash
cd ArvoreGeradoraMinima
python teste_rapido.py
```

---

## 📈 Resultados Demonstrados

### MST - Grafo Brasil

```
Cidades: 20-21
Arestas totais: 28
MST: 20 arestas
Distância total: 13.581 km
Distância se usar todas: 22.300 km
Economia: 8.719 km (39,1%)

Algoritmos: Kruskal = Prim ✓
```

---

## 💡 Destaques

### BuscaBFS/

- Busca em largura para caminho mais curto
- 20 cidades brasileiras
- Menu interativo
- Exemplos pré-definidos

### ArvoreGeradoraMinima/ ⭐ NOVO

- Dois algoritmos: Kruskal E Prim
- UnionFind com otimizações
- Ambos encontram a mesma MST
- Comparação e validação
- Análise de economia prática
- 1900+ linhas documentação

---

## ✅ Requisitos Atendidos

- [x] BFS implementado e testado
- [x] MST implementado (Kruskal + Prim)
- [x] Grafos com 20+ vértices (requisito: 16+)
- [x] Código comentado profissionalmente
- [x] Documentação extensiva
- [x] Interface interativa
- [x] Exemplos práticos
- [x] Testes automatizados

---

## 🎯 Estrutura de Documentação

Cada algoritmo possui:

1. **README.md** - Documentação completa (500+ linhas)
2. **RESUMO_EXECUTIVO.md** - Resumo 1 página
3. **GUIA_RAPIDO.md** - Quick start
4. **EXEMPLOS_VISUAIS.md** - Exemplos práticos
5. **Testes** - Validação automatizada

**Total: 1900+ linhas de documentação**

---

## 💻 Requisitos Técnicos

- Python 3.7+
- Nenhuma biblioteca externa necessária
- Terminal/Console

---

## 🎓 Para Apresentação

Cada algoritmo está pronto para apresentação com:

- Explicação teórica clara
- Demonstração prática
- Análise de complexidade
- Aplicações reais
- Exemplos funcionando

---

**Status: ✓ Completo e Validado**

Última atualização: Dezembro 2025
