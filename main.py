from gerarGraph import (
    Graph,
    WeightedDirectedGraph,
    plot_undirected_graph,
    plot_weighted_directed_graph,
)


def main():
    # Exemplo de grafo direcionado ponderado
    grafo_ponderado = WeightedDirectedGraph()
    grafo_ponderado.add_edge('A', 'B', 4)
    grafo_ponderado.add_edge('A', 'C', 2)
    grafo_ponderado.add_edge('B', 'C', 1)
    grafo_ponderado.add_edge('B', 'D', 5)
    grafo_ponderado.add_edge('C', 'D', 8)
    grafo_ponderado.add_edge('C', 'E', 10)
    grafo_ponderado.add_edge('D', 'E', 2)
    grafo_ponderado.add_edge('E', 'A', 7)
    plot_weighted_directed_graph(grafo_ponderado)

    # Exemplo de grafo não direcionado e dos métodos de Graph
    grafo = Graph()
    grafo.add_edge(0, 1)
    grafo.add_edge(0, 2)
    grafo.add_edge(0, 3)
    grafo.add_edge(1, 3)

    print("\nExemplos dos métodos de Graph:")
    print("Grau do nó 0:", grafo.degree(0))
    print("Nó com maior grau:", grafo.highest_degree())
    print("O grafo é completo?", grafo.is_Completed())

    grafo.remove_edge(0, 3)
    print("Após remover a aresta (0, 3):")
    print("Grau do nó 0:", grafo.degree(0))
    print("Grau do nó 3:", grafo.degree(3))

    plot_undirected_graph(grafo)


if __name__ == "__main__":
    main()
