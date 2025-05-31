class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        paths_dp = [1]*n
        for row in range(1, m):
            temp = paths_dp
            for col in range(1, n):
                temp[col] = paths_dp[col] + temp[col-1]
            path_dp = temp[:]
        return paths_dp[n-1]
        