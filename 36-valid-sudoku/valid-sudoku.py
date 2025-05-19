class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [0] * 9
        squares = [0] * 9
        cols = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if rows[row] & (1 << int(board[row][col])):
                    return False
                else:
                    rows[row] |= (1 << int(board[row][col]))
                
                if cols[col] & (1 << int(board[row][col])):
                    return False
                else:
                    cols[col] |= (1 << int(board[row][col]))

                square = (row//3 + (col//3) * 3)
                if squares[square] & (1 << int(board[row][col])):
                    return False
                else:
                    squares[square] |= (1 << int(board[row][col]))

        return True