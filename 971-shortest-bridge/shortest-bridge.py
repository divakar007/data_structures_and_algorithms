from collections import deque
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])
        visited = set()
        dque = deque([])

        def dfs(row, col):
            if not(0 <= row < n and 0 <= col < m):
                return 
            if grid[row][col] != 1:
                return 

            grid[row][col] += 1

            dque.append((row, col, 0))

            for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                dfs(row+x, col+y)
            


        

        for row in range(n):
            found = False
            for col in range(m):
                if grid[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break
            if found:
                break
        
        while(dque):
            r, c, curr = dque.popleft()

            visited.add((r, c))

            if grid[r][c] == 1:
                return curr
            
            if grid[r][c] == 2:
                curr = 0
            else:
                curr += 1
            for x, y in [[1,0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= r+x < n and 0 <= c+y < m and (r+x, c+y) not in visited:
                    visited.add((r+x, c+y))
                    dque.append((r+x, c+y, curr))
        

        

                     
            
            

        