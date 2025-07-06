class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0] == 1:
            return 0
        

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for i in range(m)] for i in range(n)]

        for col in range(m):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1

        for row in range(n):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1

        for row in range(1, n): 
            for col in range(1, m):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[n-1][m-1]

        