import matplotlib.pyplot as plt
import networkx as nx


class WeightedDirectedGraph:

  def __init__(self):
    self.adjList = {}

  def add_edge(self, source, sink, weight):
    if source not in self.adjList:
      self.adjList[source] = {}
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

  def remove_edge(self, u, v):
    if u in self.adjList and v in self.adjList:
      self.adjList[u].discard(v)
      self.adjList[v].discard(u)

  def degree(self, u):
    return len(self.adjList[u])

  def highest_degree(self):
    if not self.adjList:
      return None
    return max(self.adjList, key=self.degree)

  def is_Completed(self):
    nodes = len(self.adjList)
    return all(len(neighbors) == nodes - 1
               for neighbors in self.adjList.values())


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

  plt.title('Grafo NÃ£o-Direcionado')
  plt.show()
