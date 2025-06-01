class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def BuildGraph(edges):

            g = defaultdict(list)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            
            return g
        

        def getDiameter(node, graph, n):
            if n==0:
                return 0
            diameter = [0]
            visited = [0] * n
            def Diameter(node, graph):
                max1, max2 = 0, 0
                visited[node] = 1
                for adj in graph[node]:
                    if not visited[adj]:
                        count = 1 + Diameter(adj, graph)
                        if count > max1:
                            max2 = max1
                            max1 = count 
                        else:
                            if max2 < count:
                                max2 = count
                diameter[0] = max(diameter[0], max1+max2)
                return max1
            
            Diameter(node, graph)
            return diameter[0]

        g1 = BuildGraph(edges1)
        g2 = BuildGraph(edges2)

        d1 = getDiameter(0, g1, len(edges1)+1)
        d2 = getDiameter(0, g2, len(edges2)+1)

        # if len(edges1) == 0 and len(edges2) == 0:
        #     return 1
        # if len(edges1) == 0:
        #     return 1 + (d2+1)//2
        # if len(edges2) == 0:
        #     return 1 + (d1+1)//2

        return max((d1+1)//2 + (d2+1)//2 + 1,d1,d2)