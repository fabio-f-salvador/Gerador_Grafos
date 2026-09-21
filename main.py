# matriz de adjacencias
g0 = [[0, 0, 1, 0],
      [0, 0, 0, 1],
      [1, 0, 0, 1],
      [0, 1, 1, 0]]

# TODO verificar se 0 eh ligado ao 3
# print(g0[0][3] == 1)
# TODO adicionar aresta entre 0 e 1
g0[0][1] = 1
g0[1][0] = 1

# lista de adjacencias
g0 = {0: {2}, 1: {3}, 2: {0, 3}, 3: {1, 2}}

# print(3 in g0[0]) # 3 in {2} -> False
# TODO adicionar aresta entre 0 e 1
g0[0].add(1)
g0[1].add(0)

# TODO variavel que representa matriz e lista de adjacencias do grafo g1
g1 = [[0, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]

g1 = {0: {1},
      1: {0, 5},
      2: {0, 4},
      3: {1, 4},
      4: {2},
      5: {}}

g2 = [[0, 8, 0, 0, 0, 0],
      [5, 0, 0, 0, 0, 3],
      [7, 0, 0, 0, 9, 0],
      [0, 5, 0, 0, 7, 0],
      [0, 0, 6, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]

g2 = {0: {1:8},
      1: {0:5, 5:3},
      2: {0:7, 4:9},
      3: {1:5, 4:7},
      4: {2:6},
      5: {}}

from graph import WeightedDirectedGraph, Graph

g0 = WeightedDirectedGraph()
g0.add_edge(0, 1, 8)
g0.add_edge(1, 0, 5)
g0.add_edge(2, 0, 7)
g0.add_edge(2, 4, 9)
g0.add_edge(3, 1, 5)
g0.add_edge(3, 4, 7)
g0.add_edge(4, 2, 6)

g0 = Graph()
g0.add_edge(0, 2)
g0.add_edge(2, 3)
g0.add_edge(1, 3)
print(g0.adjList)

# TODO criar grafo g3 por lista de adjacencias
from graph import Graph

g3 = Graph()
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(0, 3)
g3.add_edge(1, 2)
g3.add_edge(1, 3)
g3.add_edge(2, 3)

# ou, sem orientacao a objetos:
# g3 = {0: {1, 2, 3}, 1: {0, 2, 3}, 2: {0, 1, 3}, 3: {0, 1, 2}}

# TODO implementar função que recebe um grafo, nós u e v e remove a aresta (u, v) e (v, u), se existir
print(g3.adjList)
g3.remove_edge(5, 1)
print(g3.adjList)

# TODO implementar função que recebe um grafo, um nó e retorna seu grau
assert g3.degree(2) == 3

# TODO implementar função que recebe um grafo e retorna o nó com maior grau
assert g3.highest_degree() in {0, 1, 2, 3}

g4 = Graph()
g4.add_edge(0, 1)
g4.add_edge(0, 2)
g4.add_edge(0, 3)
g4.add_edge(1, 3)
assert g4.highest_degree() == 0

assert g3.is_complete() == True
assert g4.is_complete() == False

