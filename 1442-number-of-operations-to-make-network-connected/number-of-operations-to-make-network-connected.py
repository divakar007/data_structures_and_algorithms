class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        visited = set()

        if len(connections) < n-1:
            return -1
            
        def dfs(u):
            if u not in visited:
                visited.add(u)
                for v in graph[u]:
                    dfs(v)

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0

        for u in range(n):
            if u not in visited:
                dfs(u)
                count += 1
        return count-1