from graph import DirectedGraph, UndirectedGraph


def main() -> None:
    forest = UndirectedGraph()
    forest.add_edge("A", "B", 1)
    forest.add_edge("C", "D", 1)
    print("Undirected Disconnected Forest (A-B and C-D):")
    forest.is_connected()
    forest.has_cycles()
    forest.is_tree()
    forest.is_forest()

    directed_forest = DirectedGraph()
    directed_forest.add_edge("A", "B", 1)
    directed_forest.add_edge("C", "D", 1)
    print("\nDirected Disconnected Forest (A->B and C->D):")
    directed_forest.is_connected()
    directed_forest.has_cycles()
    directed_forest.is_tree()
    directed_forest.is_forest()


if __name__ == "__main__":
    main()