class Solution:
    def solve(self, board: [[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if not (r in range(ROWS) and c in range(COLS) and board[r][c] == 'O'):
                return
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "#":
                    board[r][c] = "O"

s = Solution()
s.solve(board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])