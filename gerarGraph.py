import matplotlib.pyplot as plt
import networkx as nx

class WeightedDirectedGraph:

  def __init__(self):
    self.adjList = {}

  def add_edge(self, source, sink, weight):
    if source not in self.adjList:
      self.adjList[source] = dict()
    self.adjList[source][sink] = weight


class Graph:

  def __init__(self):
    self.adjList = {}

  def add_edge(self, source, sink):
    if source not in self.adjList:
      self.adjList[source] = set()
    self.adjList[source].add(sink)

    if sink not in self.adjList:
      self.adjList[sink] = set()
    self.adjList[sink].add(source)


def plot_weighted_directed_graph(custom_graph):
  G = nx.DiGraph()  

  for source, targets in custom_graph.adjList.items():
    for sink, weight in targets.items():
      G.add_edge(source, sink, weight=weight)

  pos = nx.spring_layout(G) 

  nx.draw(
      G,
      pos,
      with_labels=True,
      node_color='skyblue',
      node_size=2000,
      font_weight='bold',
      arrowsize=20,
  )

  edge_labels = nx.get_edge_attributes(G, 'weight')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

  plt.title('Grafo Direcionado com Pesos')
  plt.show()


def plot_undirected_graph(custom_graph):
  G = nx.Graph() 

  for source, targets in custom_graph.adjList.items():
    for sink in targets:
      G.add_edge(source, sink)

  pos = nx.spring_layout(G)

  nx.draw(
      G,
      pos,
      with_labels=True,
      node_color='lightgreen',
      node_size=2000,
      font_weight='bold',
  )

  plt.title('Grafo Não-Direcionado')
  plt.show()


# --- Exemplo de uso ---

# 1. Grafo Direcionado Ponderado
gPond = WeightedDirectedGraph()
gPond.add_edge('A', 'B', 4)
gPond.add_edge('A', 'C', 2)
gPond.add_edge('B', 'C', 1)
gPond.add_edge('B', 'D', 5)
gPond.add_edge('C', 'D', 8)
gPond.add_edge('C', 'E', 10)
gPond.add_edge('D', 'E', 2)
gPond.add_edge('E', 'A', 7)

plot_weighted_directed_graph(gPond)


# 2. Grafo Não-Direcionado
g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,3)

plot_undirected_graph(g)
