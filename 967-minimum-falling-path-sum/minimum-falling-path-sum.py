class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        min_sum_dp = [[float('inf') for i in range(cols)] for j in range(rows)]

        for col in range(cols):
            min_sum_dp[rows-1][col] = matrix[rows-1][col]

        for row in range(rows-2, -1, -1):
            for col in range(cols):
                    min_sum_dp[row][col] = matrix[row][col] +  min([min_sum_dp[row+1][col+y] if 0 <= col+y < cols else float('inf') for y in [-1, 0, 1]])
        print(min_sum_dp)
        return min(min_sum_dp[0])

