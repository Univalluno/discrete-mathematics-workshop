from graph import DirectedGraph, UndirectedGraph


def main() -> None:
    file_path = "sample.txt"

    print("1. GRAFO NO DIRIGIDO (desde sample.txt)")
    undirected = UndirectedGraph()
    undirected.load_from_file(file_path)
    print(undirected)
    undirected.is_connected()
    undirected.has_cycles()
    undirected.is_tree()
    undirected.is_forest()

    print("2. GRAFO DIRIGIDO - DAG (desde sample.txt) ")
    directed = DirectedGraph()
    directed.load_from_file(file_path)
    print(directed)
    directed.is_connected()
    directed.has_cycles()
    directed.is_tree()
    directed.is_forest()

    print("3. ARBOL DIRIGIDO (A->B, A->C)")
    directed_tree = DirectedGraph()
    directed_tree.add_edge("A", "B", 1)
    directed_tree.add_edge("A", "C", 1)
    print(directed_tree)
    directed_tree.is_connected()
    directed_tree.has_cycles()
    directed_tree.is_tree()
    directed_tree.is_forest()

    print(" 4. BOSQUE NO DIRIGIDO DISCONEXO (A-B, C-D) ===")
    forest = UndirectedGraph()
    forest.add_edge("A", "B", 1)
    forest.add_edge("C", "D", 1)
    print(forest)
    forest.is_connected()
    forest.has_cycles()
    forest.is_tree()
    forest.is_forest()


if __name__ == "__main__":
    main()