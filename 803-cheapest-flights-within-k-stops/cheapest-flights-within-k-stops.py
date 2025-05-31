class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        """
        Bellman–Ford style with at most (k+1) edge relaxations.
        
        Time Complexity: O(k * E), where E = len(flights)
        Space Complexity: O(n)
        """
        INF = float('inf')
        price = [INF] * n
        price[src] = 0
       
        for _ in range(k + 1):
            tmp = price[:]
            for u, v, w in flights:
                if price[u] != INF:
                    if price[u] + w < tmp[v]:
                        tmp[v] = price[u] + w
            price = tmp
        
        return price[dst] if price[dst] != INF else -1

            
            





        