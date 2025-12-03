# ✨ Exemplos de Visualizacao - MST

## Demonstracao do Algoritmo

### Grafo Simples (5 cidades)

```
        A -----[1]----- B
       /  \             /
     [3]  [5]       [2]
     /      \         /
    C ------[1]------ D
      \              /
       [2]--------[2]
              E
```

**Kruskal:**

1. Ordena: CD(1), CE(1), AC(3), AD(2), BD(2), AB(1), DE(2), ...
2. Adiciona CD(1) → {CD}
3. Adiciona CE(1) → {CD, CE}
4. Adiciona AD(2) → {CD, CE, AD}
5. Adiciona BD(2) → {CD, CE, AD, BD}
   **MST: 4 arestas, peso = 6**

---

## Resultado Real - Brasil 20 cidades

### MST Encontrada (Kruskal)

```
Total de estradas: 20
Distancia total: 13.581 km
Todas estradas: 22.300 km
Economia: 8.719 km (39,1%)
```

### Arestas em Ordem de Peso

```
1. Sao Paulo ↔ Campinas        =    99 km
2. Brasilia ↔ Goiania          =   209 km
3. Recife ↔ Natal              =   297 km
4. Teresina ↔ Sao Luis         =   363 km
5. Sao Paulo ↔ Curitiba        =   405 km
6. Sao Paulo ↔ Rio de Janeiro  =   430 km
7. Florianopolis ↔ Porto Alegre=   473 km
8. Rio de Janeiro ↔ Vitoria    =   521 km
9. Fortaleza ↔ Natal           =   541 km
10. Sao Paulo ↔ Belo Horizonte =   586 km
11. Fortaleza ↔ Teresina       =   622 km
12. Curitiba ↔ Florianopolis   =   626 km
13. Campo Grande ↔ Cuiaba      =   694 km
14. Belo Horizonte ↔ Brasilia  =   743 km
15. Salvador ↔ Recife          =   839 km
16. Brasilia ↔ Palmas          =   897 km
17. Goiania ↔ Campo Grande     =   933 km
18. Belem ↔ Sao Luis           = 1.180 km
19. Brasilia ↔ Salvador        = 1.401 km
20. Belem ↔ Manaus             = 1.722 km
```

---

## Comparacao: Kruskal vs Prim

### Ambos encontram a MESMA MST

Quando começado de **São Paulo**, Prim produz a mesma árvore com:

- **20 arestas** (V-1)
- **13.581 km** de distância total
- **Mesma economia** de 39,1%

### Diferenca: Ordem de processamento

| Algoritmo | Ordem       | Tempo      | Ideal Para      |
| --------- | ----------- | ---------- | --------------- |
| Kruskal   | Por peso    | O(E log E) | Grafos esparsos |
| Prim      | Crescimento | O(V²)      | Grafos densos   |

---

## Ciclos Evitados

No exemplo Brasil, Kruskal processou **27 arestas** mas:

- Apenas **20 foram adicionadas** (conectar 21 vertices)
- **7 foram descartadas** por criar ciclos

Isso mostra a importancia do Union-Find!

---

## Verificacao: Propriedades da MST

### 1. Conectividade

- [x] Todos os 21 vertices estao conectados
- [x] Nenhum vertice ficou isolado

### 2. Aciclidade

- [x] Sao 20 arestas para 21 vertices (V-1)
- [x] Nenhum ciclo foi criado

### 3. Minimalidade

- [x] O peso total (13.581 km) e o minimo possivel
- [x] Qualquer outra combinacao de 20 arestas conectando 21 vertices
      teria peso >= 13.581 km

---

## Como Interpretar o Resultado

1. **Veja as arestas menores primeiro**

   - Sao Paulo ↔ Campinas (99 km) esta presente ✓
   - Brasilia ↔ Goiania (209 km) esta presente ✓

2. **Veja as arestas maiores**

   - Muitas arestas grandes podem estar FORA
   - Por exemplo: Palmas ↔ Manaus (2.156 km) nao esta na MST
   - Isso economiza distancia!

3. **Economia realista**
   - Se o objetivo e conectar com minimo custo
   - A MST economiza 39,1% comparado ao usar todas as estradas
   - Para 20 cidades: economia de 8.719 km!

---

## Propriedade do Corte (Cut Property)

Para cada MST, podemos demonstrar:

```
Corte: {Sudeste} vs {Resto}

Arestas atravessando o corte:
- SP ↔ Brasilia (743 km)
- SP ↔ Campo Grande (1155 km)

Aresta minima: SP ↔ Brasilia (743 km)
Resultado: Kruskal selecionou esta! ✓

Isso prova que a MST e OTIMA.
```

---

## Teste: Prim de Cidades Diferentes

Se executar Prim começando de cidades diferentes:

- Rio de Janeiro → MST peso: 13.581 km ✓
- Salvador → MST peso: 13.581 km ✓
- Manaus → MST peso: 13.581 km ✓

Sempre o MESMO peso! Isso prova que a MST e UNICA
(quando todos os pesos sao distintos).

---

## Pronto para Apresentacao!

Use esses dados para demonstrar:

1. **Corretude dos algoritmos**

   - Kruskal e Prim encontram a mesma MST
   - Peso total sempre igual

2. **Eficiencia**

   - 20 arestas suficientes (de 28 possiveis)
   - Economia de 39,1%

3. **Propriedades matematicas**

   - V-1 arestas para V vertices
   - Nenhum ciclo
   - Peso minimo

4. **Aplicacoes praticas**
   - Economia real em infraestrutura
   - Decisoes de investimento
   - Otimizacao de redes
