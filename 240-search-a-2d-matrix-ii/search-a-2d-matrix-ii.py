class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n = len(matrix)
        m = len(matrix[0])

        row, col = 0, m-1
        while (0 <=row < n and 0 <= col < m):
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False
        