class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = self.buildGraph(n, invocations)
        suspicious = self.findSuspiciousMethods(k, graph)
        
        if self.canRemoveSafely(suspicious, invocations):
            return self.getNonSuspiciousMethods(n, suspicious)
        else:
            return list(range(n))  # can't safely remove; keep all
    
    def buildGraph(self, n: int, invocations: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)  # directed edge: u invokes v
        return adj
    
    def findSuspiciousMethods(self, k: int, graph: List[List[int]]) -> set:
        visited = set()
        queue = [k]
        visited.add(k)
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited  # all methods reachable from k
    
    def canRemoveSafely(self, suspicious: set, invocations: List[List[int]]) -> bool:
        for u, v in invocations:
            if u not in suspicious and v in suspicious:  # outside → inside edge blocks removal
                return False
        return True
    
    def getNonSuspiciousMethods(self, n: int, suspicious: set) -> List[int]:
        return [i for i in range(n) if i not in suspicious]