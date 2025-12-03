# ⚡ Guia Rápido - MST

## 🚀 Começo Rápido

```bash
python mst_cidades.py
```

---

## 📋 Menu Principal

```
1. Executar Algoritmo de Kruskal
2. Executar Algoritmo de Prim
3. Comparar Kruskal vs Prim
4. Ver mapa de estradas novamente
5. Sair
```

---

## 🎯 O Que Cada Algoritmo Faz

### Kruskal

- Ordena arestas por peso
- Adiciona sem criar ciclos
- Ordem: menor peso primeiro

### Prim

- Escolhe um vértice inicial
- Cresce a árvore passo a passo
- Sempre a menor aresta disponível

---

## 📊 Entenda a Saída

### Fase 1: Construção do Grafo

```
✓ Cidade 'São Paulo' adicionada
✓ Estrada: São Paulo ↔ Rio de Janeiro (430 km)
...
Total de cidades: 20
Total de arestas: 28
```

### Fase 2: Execução do Algoritmo

```
ALGORITMO DE KRUSKAL
✓ ADICIONA: São Paulo ↔ Campinas (99 km) - MST agora tem 1 arestas
✓ ADICIONA: Brasília ↔ Goiânia (209 km) - MST agora tem 2 arestas
...
```

### Fase 3: Resultado Final

```
RESULTADO - ÁRVORE GERADORA MÍNIMA
  1. São Paulo ↔ Campinas | 99.0 km
  2. Brasília ↔ Goiânia | 209.0 km
  ...
RESUMO DA MST:
   Total de estradas: 19
   Distância total: 10,847 km
```

---

## 🔍 Analisando o Resultado

### O que é V-1?

- V = número de vértices (cidades)
- Uma MST sempre tem exatamente V-1 arestas
- Para 20 cidades → 19 estradas

### Ganho de Economia

```
Se conectar TODAS as estradas: 15,326 km
MST (Mínima): 10,847 km
Economia: 4,479 km (29%)
```

---

## 🔄 Comparar os Dois Algoritmos

**Opção 3 do menu executa ambos e mostra:**

- Peso Kruskal: X km
- Peso Prim: X km
- Diferença: 0.0 km ✓

**Conclusão:** Mesma MST, ordem diferente!

---

## 🐛 Se Algo Der Errado

| Problema          | Solução                |
| ----------------- | ---------------------- |
| "ModuleError"     | Python 3.7+ instalado? |
| Menu não funciona | Digite apenas 1-5      |
| Grafo vazio       | Reinicie o programa    |

---

## 💾 Estruturas Principais

### Classe Aresta

```python
Aresta(origem="A", destino="B", peso=100)
```

### Classe GrafoMST

```python
grafo = GrafoMST()
grafo.adicionar_estrada("A", "B", 100)
resultado = grafo.kruskal()
```

### UnionFind

```python
uf = UnionFind({"A", "B", "C"})
uf.union("A", "B")
if uf.sao_conectados("A", "B"):
    print("Conectados!")
```

---

## 📝 Código Essencial

### Usar Kruskal

```python
grafo = criar_mapa_brasil_ponderado()
resultado = grafo.kruskal()
if resultado:
    arestas, peso = resultado
    grafo.exibir_mst(arestas, peso, "Kruskal")
```

### Usar Prim

```python
grafo = criar_mapa_brasil_ponderado()
resultado = grafo.prim("São Paulo")  # de um vértice
if resultado:
    arestas, peso = resultado
    grafo.exibir_mst(arestas, peso, "Prim")
```

---

## ⚙️ Parâmetros

### Kruskal

- **Sem parâmetros obrigatórios**
- Sempre encontra a MST global

### Prim

- **Parâmetro:** `inicio` (opcional)
- Se não informado, usa primeira cidade
- Resultado é o mesmo independente da origem

---

## 📈 Complexidade Rápido

| Algoritmo | Tempo      | Espaço |
| --------- | ---------- | ------ |
| Kruskal   | O(E log E) | O(V+E) |
| Prim      | O(V²)      | O(V)   |

**E** = arestas | **V** = vértices

---

## 🎯 Lembrete Importante

✅ Kruskal e Prim encontram **MESMA MST**
✅ Peso total será **IGUAL**
✅ Ordem das arestas pode ser **DIFERENTE**
✅ Ambos são **ÓTIMOS**

---

## 🔗 Próximos Passos

1. Execute o programa
2. Experimente ambos os algoritmos
3. Compare os resultados
4. Leia o README completo
5. Estude o código comentado

**Pronto! Você está usando MST!** 🚀
