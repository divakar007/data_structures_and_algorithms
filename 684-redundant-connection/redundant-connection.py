class DisjointSet():

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False

        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        else:
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1

        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = max([max(u, v) for u, v in edges])+1
        ds = DisjointSet(n)

        for u,v in edges:
            if not ds.union(u,v):
                return [u, v]
        return -1