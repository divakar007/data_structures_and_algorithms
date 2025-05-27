class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self.parent[pv] = pu
        return True

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = {}
        cand1 = cand2 = None

        # Step 1: Check if a node has two parents
        for u, v in edges:
            if v in parent:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
            parent[v] = u
        
        # Step 2: Union-Find to detect cycles
        ds = DisjointSet(n + 1)
        for u, v in edges:
            if [u, v] == cand2:
                continue  # Skip second parent edge temporarily
            if not ds.union(u, v):
                # Cycle found
                return cand1 if cand1 else [u, v]

        # No cycle but there was a node with two parents
        return cand2
