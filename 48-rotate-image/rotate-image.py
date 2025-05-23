class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r+1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in range(rows):
            r = len(matrix[row])
            for i in range(r//2):
                matrix[row][i], matrix[row][r-i-1] = matrix[row][r-i-1], matrix[row][i]
                


        
        