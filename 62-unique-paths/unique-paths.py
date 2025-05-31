class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        paths_dp = [[1]*n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                paths_dp[row][col] = paths_dp[row-1][col] + paths_dp[row][col-1]
        return paths_dp[m-1][n-1]
        