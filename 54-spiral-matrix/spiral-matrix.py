class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        right = left = up = down = False

        right = True
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        row = col = 0

        seen = 0

        def isWall(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return True
            return matrix[row][col] == None

        while seen < rows*cols:
            seen += 1
            res.append(matrix[row][col])
            matrix[row][col] = None

            if right:
                if isWall(row, col+1):
                    right = False
                    down = True
                    row += 1
                else:
                    col += 1
            elif left:
                if isWall(row, col-1):
                    left = False
                    up = True
                    row -= 1
                else:
                    col -= 1
            elif up:
                if isWall(row-1, col):
                    up = False
                    right = True
                    col += 1
                else:
                    row -= 1
            elif down:
                if isWall(row+1, col):
                    down = False
                    left = True
                    col -= 1
                else:
                    row += 1
    
        return res
        




