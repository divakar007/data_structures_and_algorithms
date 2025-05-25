from collections import deque
import heapq as hq
class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        minheap = ([(0,0,0)])
        n = len(grid)
        m = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1  

        while minheap:
            currT, row, col = hq.heappop(minheap)

            if row == n-1 and col == m-1:
                return currT

            if (row, col) not in visited:
                visited.add((row, col))
                for x, y in directions:
                    next_row, next_col = x+row, y+col
                    if 0 <= next_row < n and 0 <= next_col < m:
                        wait_time = (1 if (grid[next_row][next_col] - currT) % 2 == 0 else 0)
                        next_time = max(grid[next_row][next_col] + wait_time, currT + 1)
                        heapq.heappush(minheap, (next_time, next_row, next_col))

            
        return -1

        


