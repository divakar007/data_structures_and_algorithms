class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """

        def distance(bomb1, bomb2):
            x1, y1, r1 = bomb1
            x2, y2, r2 = bomb2
            return ((x2-x1)**2 + (y1-y2)**2)**0.5

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if distance(bombs[i], bombs[j]) <= bombs[i][2]:
                    graph[i].append(j)
        
        nodes = list(range(len(bombs)))

        def dfs(node, visited):
            visited.add(node)
            count = 0
            for nxt in graph[node]:
                if nxt not in visited:
                    count += (1 + dfs(nxt, visited))
            return count

        maxCount = 0
        for i in range(len(bombs)):
            maxCount = max(maxCount, 1+dfs(i,set()))
        
        return maxCount



                
    
    
        