class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.buildGraph(n, edges)
        components = self.findAllComponents(graph, n)

        complete_count = 0
        for component in components:
            if self.isCompleteComponent(component, graph):
                complete_count += 1

        return complete_count

    def buildGraph(self, n: int, edges: List[List[int]]) -> List[set]:
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return graph

    def findAllComponents(self, graph: List[set], n: int) -> List[List[int]]:
        visited = [False] * n
        components = []
        for i in range(n):
            if not visited[i]:
                component = self.bfs(i, graph, visited)
                components.append(component)
        return components

    def bfs(self, start: int, graph: List[set], visited: List[bool]) -> List[int]:
        from collections import deque
        queue = deque([start])
        visited[start] = True
        component = []
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    def isCompleteComponent(self, component: List[int], graph: List[set]) -> bool:
        k = len(component)
        expected_edges = k * (k - 1) // 2
        actual_edges = 0
        for node in component:
            for neighbor in graph[node]:
                if neighbor in component:
                    actual_edges += 1
        actual_edges //= 2  # each edge counted twice
        return actual_edges == expected_edges