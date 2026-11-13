from collections import deque


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

    def _is_connected(self) -> bool:
        if not self.adjacency_list:
            return False

        start_vertex = next(iter(self.adjacency_list))
        visited: set[str] = {start_vertex}
        queue: deque[str] = deque([start_vertex])

        while queue:
            current = queue.popleft()
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == len(self.adjacency_list)

    def _has_cycles(self) -> bool:
        visited: set[str] = set()

        def dfs(vertex: str, parent: str | None) -> bool:
            visited.add(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor == vertex:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for vertex in self.adjacency_list:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    def _is_tree(self) -> bool:
        return self._is_connected() and not self._has_cycles()

    def _is_forest(self) -> bool:
        if not self.adjacency_list:
            return False
        return not self._has_cycles()

    def is_connected(self) -> bool:
        result = self._is_connected()
        print(f"{self.is_connected.__name__}: {result}")
        return result

    def has_cycles(self) -> bool:
        result = self._has_cycles()
        print(f"{self.has_cycles.__name__}: {result}")
        return result

    def is_tree(self) -> bool:
        result = self._is_tree()
        print(f"{self.is_tree.__name__}: {result}")
        return result

    def is_forest(self) -> bool:
        result = self._is_forest()
        print(f"{self.is_forest.__name__}: {result}")
        return result

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

    def _get_in_degrees(self) -> dict[str, int]:
        in_degrees: dict[str, int] = {vertex: 0 for vertex in self.adjacency_list}
        for neighbors in self.adjacency_list.values():
            for target in neighbors:
                in_degrees[target] += 1
        return in_degrees

    def _is_connected(self) -> bool:
        if not self.adjacency_list:
            return False

        undirected_neighbors: dict[str, set[str]] = {
            vertex: set() for vertex in self.adjacency_list
        }
        for source, targets in self.adjacency_list.items():
            for target in targets:
                undirected_neighbors[source].add(target)
                undirected_neighbors[target].add(source)

        start_vertex = next(iter(self.adjacency_list))
        visited: set[str] = {start_vertex}
        queue: deque[str] = deque([start_vertex])

        while queue:
            current = queue.popleft()
            for neighbor in undirected_neighbors[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == len(self.adjacency_list)

    def _has_cycles(self) -> bool:
        # 0 = unvisited, 1 = visiting (in recursion stack), 2 = visited
        state: dict[str, int] = {vertex: 0 for vertex in self.adjacency_list}

        def dfs(vertex: str) -> bool:
            state[vertex] = 1
            for neighbor in self.adjacency_list[vertex]:
                if state[neighbor] == 1:
                    return True
                if state[neighbor] == 0 and dfs(neighbor):
                    return True
            state[vertex] = 2
            return False

        for vertex in self.adjacency_list:
            if state[vertex] == 0:
                if dfs(vertex):
                    return True
        return False

    def _is_tree(self) -> bool:
        if not self.adjacency_list or self._has_cycles():
            return False

        in_degrees = self._get_in_degrees()
        roots = [vertex for vertex, degree in in_degrees.items() if degree == 0]
        if len(roots) != 1:
            return False

        return all(degree == 1 for vertex, degree in in_degrees.items() if vertex != roots[0])

    def _is_forest(self) -> bool:
        if not self.adjacency_list or self._has_cycles():
            return False

        in_degrees = self._get_in_degrees()
        return all(degree <= 1 for degree in in_degrees.values())

    def get_out_degree(self, vertex: str) -> int:
        return len(self.adjacency_list.get(vertex, {}))

    def get_in_degree(self, vertex: str) -> int:
        if vertex not in self.adjacency_list:
            return 0
        return sum(1 for neighbors in self.adjacency_list.values() if vertex in neighbors)