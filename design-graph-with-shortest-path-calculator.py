import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = defaultdict(list)
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: list[int]) -> None:
        fr, to, cost = edge
        self.graph[fr].append((to, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visited = set()
        while heap:
            cost, node = heapq.heappop(heap)
            visited.add(node)
            if node == node2:
                return cost
            for i, j in self.graph[node]:
                if i not in visited:
                    heapq.heappush(heap, (cost + j, i))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)