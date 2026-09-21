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

    def remove_edge(self, u, v):
        try:
            self.adjList[u].remove(v)
            self.adjList[v].remove(u)
        except KeyError:
            print(f"Node {u} or {v} not found")

    def degree(self, u):

        return len(self.adjList[u])

    def highest_degree(self):
        max_degree = -1
        max_node = None
        for u in self.adjList:
            if self.degree(u) > max_degree:
                max_degree = self.degree(u)
                max_node = u

        return max_node

    def is_Completed(self):
        nodes = len(self.adjList)
        for u in self.adjList:
            neighbors_of_u = len(self.adjList[u])
            if nodes - 1 != neighbors_of_u:
                return False

        return True