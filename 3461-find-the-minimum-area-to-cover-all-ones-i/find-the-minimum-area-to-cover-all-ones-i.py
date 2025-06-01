class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

        m = len(grid)
        n = len(grid[0])
        min_i, min_j, max_i, max_j = m, n, 0, 0

        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    min_i = min(min_i, row)
                    min_j = min(min_j, col)
                    max_i = max(max_i, row)
                    max_j = max(max_j, col)
        return (max_i-min_i+1) * (max_j-min_j+1)

                    