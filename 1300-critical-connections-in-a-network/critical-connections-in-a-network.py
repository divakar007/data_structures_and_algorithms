class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list) 
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        lowestTime = [float('inf') for i in range(n)]
        currTime = [0] * (n)
        time = [1]
        bridges = []
        def dfs(node, parent, lowestTime, currTime, visited, time):

            visited[node] = 1
            currTime[node] = time[0]
            lowestTime[node] = time[0]

            time[0] += 1

            for adj in graph[node]:
                if adj != parent:
                    if visited[adj] == 0:
                        dfs(adj, node, lowestTime, currTime, visited, time)
                        lowestTime[node] = min(lowestTime[node], lowestTime[adj]) 

                        if lowestTime[adj] > currTime[node]:
                            bridges.append([node, adj])
                    else:
                        lowestTime[node] = min(lowestTime[node], lowestTime[adj]) 

        visited = [0] * n
        dfs(0, -1, lowestTime, currTime, visited, time)

        return bridges


