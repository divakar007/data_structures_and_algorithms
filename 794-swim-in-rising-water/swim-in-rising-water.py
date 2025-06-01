class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq as hq
        n = len(grid)
        que = [(grid[0][0], 0, 0)]
        visited = [[0] * n for _ in range(n)]
        while que:
            curr_depth, x, y = hq.heappop(que)
            
            if visited[x][y]:
                continue

            visited[x][y] = 1


            if x == n-1 and y == n-1:
                return curr_depth

            for inc_x, inc_y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= x+inc_x < n and 0 <= y + inc_y < n:
                    hq.heappush(que, (max(curr_depth, grid[x+inc_x][y+inc_y]), x + inc_x, y + inc_y)) 
        



        