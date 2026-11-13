class UndirectedGraph:
    def __init__(self) -> None:
        self.adjacency_list: dict[str, dict[str, int | float]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, source: str, target: str, weight: int | float = 1) -> None:
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency_list[source][target] = weight
        self.adjacency_list[target][source] = weight

    def load_from_file(self, file_path: str) -> None:
        self.adjacency_list.clear()
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = [item.strip() for item in clean_line.split(",")]
                if len(parts) >= 2 and parts[0].lower() == "source" and parts[1].lower() == "target":
                    continue

                if len(parts) == 1:
                    self.add_vertex(parts[0])
                    continue

                source = parts[0]
                target = parts[1]
                raw_weight = parts[2] if len(parts) > 2 else "1"
                weight: int | float = (
                    int(raw_weight) if raw_weight.lstrip("-").isdigit() else float(raw_weight)
                )
                self.add_edge(source, target, weight)

    def get_vertices(self) -> list[str]:
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex: str) -> dict[str, int | float]:
        return self.adjacency_list.get(vertex, {})

    def __str__(self) -> str:
        lines = []
        for vertex, neighbors in self.adjacency_list.items():
            lines.append(f"{vertex}: {neighbors}")
        return "\n".join(lines)


class DirectedGraph(UndirectedGraph):
    def add_edge(self, source: str, target: str, weight: int | float = 1) -> None:
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency_list[source][target] = weight

    def get_out_degree(self, vertex: str) -> int:
        return len(self.adjacency_list.get(vertex, {}))

    def get_in_degree(self, vertex: str) -> int:
        if vertex not in self.adjacency_list:
            return 0
        return sum(1 for neighbors in self.adjacency_list.values() if vertex in neighbors)