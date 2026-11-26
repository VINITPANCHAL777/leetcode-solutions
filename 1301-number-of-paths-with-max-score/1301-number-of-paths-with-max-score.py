
class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        # Maximum score and number of ways
        dp = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        # Start from E
        dp[0][0] = 0
        ways[0][0] = 1

        # Traverse from top-left to bottom-right
        for i in range(n):
            for j in range(n):

                if board[i][j] == 'X' or dp[i][j] == -1:
                    continue

                # Move down, right, diagonal
                directions = [
                    (i + 1, j),
                    (i, j + 1),
                    (i + 1, j + 1)
                ]

                for ni, nj in directions:

                    if ni >= n or nj >= n:
                        continue

                    if board[ni][nj] == 'X':
                        continue

                    # Add destination cell value
                    value = 0
                    if board[ni][nj].isdigit():
                        value = int(board[ni][nj])

                    new_score = dp[i][j] + value

                    if new_score > dp[ni][nj]:
                        dp[ni][nj] = new_score
                        ways[ni][nj] = ways[i][j]

                    elif new_score == dp[ni][nj]:
                        ways[ni][nj] = (
                            ways[ni][nj] + ways[i][j]
                        ) % MOD

        if dp[n-1][n-1] == -1:
            return [0, 0]

        return [dp[n-1][n-1], ways[n-1][n-1]]
