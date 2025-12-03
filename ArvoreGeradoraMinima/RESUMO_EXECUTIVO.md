# 📌 Resumo Executivo - MST (Minimum Spanning Tree)

## 🎯 Objetivo em Uma Frase

Conectar todas as cidades com o menor custo/distância total possível.

---

## 🔑 Conceitos Chave

### O que é MST?

- **Árvore Geradora Mínima** = subconjunto de arestas que:
  - Conecta todos os vértices
  - Não contém ciclos
  - Tem peso total mínimo

### Propriedade Fundamental

Para um grafo com **V** vértices, uma MST sempre tem exatamente **V-1 arestas**.

### Exemplo

```
Grafo com 5 cidades, 7 estradas
Se conectar TODAS: 7 estradas
MST: 4 estradas (com custo mínimo)
```

---

## ⚡ Dois Algoritmos

### 🥇 Algoritmo de Kruskal

**Abordagem:** Gulosa com ordenação

```
1. Ordena TODAS as arestas por peso
2. Para cada aresta (menor primeiro):
   - Se NÃO criar ciclo, adiciona à MST
   - Senão, descarta
3. Para quando tiver V-1 arestas
```

**Complexidade:** O(E log E)
**Melhor para:** Grafos esparsos
**Estrutura:** Union-Find para detectar ciclos

### 🥈 Algoritmo de Prim

**Abordagem:** Crescimento incremental

```
1. Começa com um vértice qualquer
2. Repete V-1 vezes:
   - Encontra menor aresta que conecta
     MST atual a vértice novo
   - Adiciona à MST
```

**Complexidade:** O(V²)
**Melhor para:** Grafos densos
**Estrutura:** Set de vértices visitados

---

## 🔄 Comparação Rápida

| Critério   | Kruskal     | Prim          |
| ---------- | ----------- | ------------- |
| Velocidade | O(E log E)  | O(V²)         |
| Começa     | Não importa | De um vértice |
| Estrutura  | Union-Find  | Set           |
| Ideal      | Esparso     | Denso         |
| Resultado  | Mesma MST   | Mesma MST     |

---

## 💡 Exemplo Prático (4 cidades)

### Grafo

```
    A ----5---- B
    |           |
    3           2
    |           |
    C ----1---- D
```

### Kruskal

```
1. Ordena: CD(1), BD(2), AC(3), AB(5)
2. Adiciona CD → {CD}
3. Adiciona BD → {CD, BD}
4. Adiciona AC → {CD, BD, AC} ✓ PRONTO (3 arestas)

MST = {AC, BD, CD}, peso = 1+2+3 = 6
```

### Prim (começando em A)

```
1. Começa: A
2. Menor aresta de A: AC(3) → {A, C}
3. Menor aresta A,C p/ novo: CD(1) → {A, C, D}
4. Menor aresta A,C,D p/ novo: BD(2) → {A, C, D, B} ✓ PRONTO

MST = {AC, CD, BD}, peso = 1+2+3 = 6
```

**Resultado:** Mesma MST, ordem diferente! ✓

---

## 🏆 Quando Usar

### Use Kruskal se:

- ✓ Grafo é esparso (poucas arestas)
- ✓ Arestas já estão disponíveis em lista
- ✓ Quer algoritmo simples de entender

### Use Prim se:

- ✓ Grafo é denso (muitas arestas)
- ✓ Grafos muito grandes (V² é melhor que E log E)
- ✓ Precisa começar de vértice específico

---

## 📊 Aplicações Reais

| Área                | Aplicação              |
| ------------------- | ---------------------- |
| 🏗️ Infraestrutura   | Redes de estradas      |
| 🌐 Telecomunicações | Cabos de fibra óptica  |
| 💡 Energia          | Distribuição elétrica  |
| 🖥️ Redes            | Roteamento otimizado   |
| 🚇 Transporte       | Planejamento de linhas |

---

## 🚀 Como Executar

```bash
python mst_cidades.py
```

Menu interativo com opções:

1. Kruskal
2. Prim
3. Comparar ambos
4. Ver mapa
5. Sair

---

## 📈 Resultado Esperado

```
📊 RESUMO DA MST:
   Total de estradas: 19 (de 28 possíveis)
   Distância total: ~10,800 km
   Economia: ~4,500 km (29%)
```

---

## ✨ Destaques

✅ Ambos os algoritmos encontram a **mesma MST** com **mesmo peso**
✅ A ordem de arestas na MST pode ser diferente
✅ Se todos os pesos forem distintos, a MST é **única**
✅ Funciona em tempo **polinomial** (não NP-completo)

---

## 🎓 Pontos de Apresentação

1. **Definir MST claramente** (V-1 arestas, sem ciclos)
2. **Explicar Kruskal** (ordena, depois constrói)
3. **Explicar Prim** (cresce incrementalmente)
4. **Mostrar que encontram a mesma MST**
5. **Demonstrar com exemplo real** (20 cidades brasileiras)
6. **Comparar complexidades**
7. **Aplicações práticas**

---

**Para mais detalhes, veja o README completo!** 📖
