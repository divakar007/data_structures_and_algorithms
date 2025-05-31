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
        no_of_edges = len(flights)

        graph = defaultdict(list)

        for s, d, p in flights:
            graph[s].append((d, p))
        
        prices = [float('inf')] * n 
        prices[src] = 0

        dq = deque([(src, 0, 0)])

        while dq:
            current_source, curr_price, curr_k = dq.popleft()
            if curr_k > k:
                continue
            for next_source,next_price in graph[current_source]:
                new_price=next_price+curr_price
                if new_price<prices[next_source]:
                    prices[next_source]=new_price
                    dq.append((next_source,new_price,curr_k+1))
                    
        
        return prices[dst] if prices[dst] != float('inf') else -1
            
            





        