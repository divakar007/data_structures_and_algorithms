class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        board_copy = [[i for i in board[r]] for r in range(rows)]
        def get_neighbours(row, col):
            x = [-1, 0, 1]
            curr_n = 0
            for i in x:
                for j in x:
                    if i == j == 0:
                        continue
                    if 0 <= row + i  < rows and 0 <= col + j < cols:
                        curr_n += board_copy[row + i][col + j]
            return curr_n

        for r in range(rows):
            for c in range(cols):
                curr = get_neighbours(r, c)
                if board[r][c] == 1:
                    if curr < 2 or curr > 3:
                        board[r][c] = 0
                else:
                    if curr == 3:
                        board[r][c] = 1
            

        