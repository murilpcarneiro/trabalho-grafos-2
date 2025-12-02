# Dijkstra - Capitais do Brasil

## Descrição
Este projeto implementa o **Algoritmo de Dijkstra** em Python puro (sem bibliotecas externas) para encontrar o caminho mais curto entre as capitais dos estados brasileiros.

## Características

✅ **Algoritmo de Dijkstra** implementado do zero, sem uso de bibliotecas externas
✅ **Grafo com 27 capitais brasileiras** (26 estados + DF)
✅ **Distâncias reais aproximadas** entre as cidades em Km
✅ **Interface gráfica interativa** com Tkinter
✅ **Visualização do caminho** encontrado no mapa
✅ **Seleção de origem e destino** via dropdown
✅ **Cálculo automático** da distância mínima

## Estrutura de Arquivos

```
Dijkstra/
├── dijkstra_algoritmo.py      # Implementação pura do algoritmo
├── capitais_brasil.py          # Base de dados das capitais e distâncias
├── interface_interativa.py     # Interface gráfica com Tkinter
└── README.md                   # Este arquivo
```

## Uso

### Executar a Interface Interativa
```bash
python interface_interativa.py
```

### Como Usar
1. Selecione uma **Origem** no primeiro dropdown
2. Selecione um **Destino** no segundo dropdown
3. Clique em **"Calcular Caminho"**
4. O algoritmo de Dijkstra calcula o caminho mais curto
5. O resultado mostra:
   - **Distância Total** em Km
   - **Caminho completo** (sequência de cidades)
   - **Visualização no mapa** com o percurso destacado em vermelho

## Cores no Mapa
- 🟢 **Verde**: Cidade de origem
- 🔴 **Vermelho**: Cidade de destino
- 🟠 **Laranja**: Cidades no caminho encontrado
- 🔵 **Azul claro**: Outras cidades
- 🔴 **Linhas vermelhas**: Arestas do caminho mais curto
- ⚫ **Linhas cinzas**: Outras conexões disponíveis

## Algoritmo de Dijkstra - Como Funciona

O algoritmo funciona em 4 etapas:

1. **Inicialização**: Define distância 0 para o nó inicial e infinito para os demais
2. **Seleção**: Escolhe o nó não visitado com menor distância
3. **Atualização**: Atualiza as distâncias dos vizinhos
4. **Repetição**: Repete até alcançar o destino ou esgotar todos os nós

### Complexidade
- **Tempo**: O(n²) onde n = número de vértices
- **Espaço**: O(n) para armazenar distâncias e antecessores

## Exemplo de Uso

```
Origem: São Paulo
Destino: Rio de Janeiro

Resultado:
Distância Total: 429 km
Caminho: São Paulo → Rio de Janeiro
```

## Capitais Incluídas

```
AC - Rio Branco         MT - Cuiabá
AL - Maceió             MS - Campo Grande
AP - Macapá             MG - Belo Horizonte
AM - Manaus             PA - Belém
BA - Salvador           PB - João Pessoa
CE - Fortaleza          PR - Curitiba
DF - Brasília           PE - Recife
ES - Vitória            RJ - Rio de Janeiro
GO - Goiânia            RN - Natal
MA - São Luís           RS - Porto Alegre
                        RR - Boa Vista
                        SP - São Paulo
                        SE - Aracaju
                        TO - Palmas
```

## Requisitos
- Python 3.6+
- Tkinter (geralmente incluído com Python)

## Notas Técnicas

### Sobre as Distâncias
As distâncias foram aproximadas com base em coordenadas lat/lon e ajustes para rotas reais. Não são distâncias precisas mas representam bem a malha viária brasileira.

### Por que Sem Bibliotecas Externas?
O algoritmo foi implementado usando apenas estruturas de dados básicas do Python:
- Dicionários para o grafo de adjacência
- Listas para manter nós não visitados
- Conjuntos para nós visitados

Isso permite compreender exatamente como o algoritmo funciona sem abstrações de bibliotecas.

## Autor
Implementação para fins educacionais - trabalho de Grafos
