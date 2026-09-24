class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(m):
            for j in range(n):
                live = 0

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        # 1 = currently alive
                        # 2 = currently alive, will die
                        # 3 = currently dead, will become alive
                        if board[ni][nj] == 1 or board[ni][nj] == 2:
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2
                else:
                    if live == 3:
                        board[i][j] = 3

        # Convert temporary states to next generation
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1