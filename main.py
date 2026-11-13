from graph import DirectedGraph, UndirectedGraph


def main() -> None:
    undirected = UndirectedGraph()
    undirected.load_from_file("sample.txt")
    print("Undirected Graph loaded from file:")
    print(undirected)

    directed = DirectedGraph()
    directed.load_from_file("sample.txt")
    print("\nDirected Graph loaded from file:")
    print(directed)


if __name__ == "__main__":
    main()