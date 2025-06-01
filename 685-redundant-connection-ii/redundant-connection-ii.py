class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        # Step 1: check for a node with two parents
        parent = [0]*(n+1)
        cand1 = cand2 = None
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                # v already has a parent: record both edges
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break

        def union_find(skip_edge):
            ds = DisjointSet(n+1)
            for x, y in edges:
                if [x, y] == skip_edge:
                    continue
                if not ds.union(x, y):
                    return False  # found a cycle
            return True

        # If there was a node with two parents, try skipping cand2:
        if cand2:
            # If skipping cand2 yields a valid tree, cand2 is the answer.
            if union_find(cand2):
                return cand2
            # Otherwise, cand1 is the edge to remove.
            return cand1

        # Otherwise, no node has two parents: just detect the edge that closes a cycle
        ds = DisjointSet(n+1)
        for u, v in edges:
            if not ds.union(u, v):
                return [u, v]

