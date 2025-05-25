class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for _ in range(n)] 
        def dfs(x, y, vis, grid):
            if x >= n or y >= m or x < 0 or y < 0:
                return 
            if grid[x][y] == "0":
                return 
            
            if vis[x][y]:
                return
            
            vis[x][y] = 1
            
            dfs(x+1, y, vis, grid) 
            dfs(x, y+1, vis, grid)
            dfs(x-1, y, vis, grid)
            dfs(x, y-1, vis, grid)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j]=="1":
                    dfs(i, j, vis, grid)
                    count += 1
        return count
        

        