'''
Time complexity O(n!)
Space complexity O(n)
TODO: NQueens2
'''
class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        ans = []

        def tryRow(row, board, column_used, diag1_used, diag2_used):
            if row == N:
                current = []
                for r in board:
                    current.append("".join(r))
                ans.append(current)
                return

            for col in range(N):
                if col not in column_used and row + col not in diag1_used and row - col not in diag2_used:
                    board[row][col] = "Q"
                    column_used.add(col)
                    diag1_used.add(row + col)
                    diag2_used.add(row - col)
                    tryRow(row + 1, board, column_used, diag1_used, diag2_used)
                    board[row][col] = "."
                    column_used.remove(col)
                    diag1_used.remove(row + col)
                    diag2_used.remove(row - col)

        board = [["."] * N for _ in range(N)]
        tryRow(0, board, set(), set(), set())
        return ans

        