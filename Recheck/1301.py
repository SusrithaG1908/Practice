from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # score[i][j] = maximum score to reach (i,j) from S
        score = [[-1] * n for _ in range(n)]

        # ways[i][j] = number of paths with maximum score
        ways = [[0] * n for _ in range(n)]

        # Start from S
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        # Fill DP from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Skip obstacle and start cell
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                count = 0

                # Check below, right, and diagonal
                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if ni < n and nj < n and ways[ni][nj] > 0:

                        if score[ni][nj] > best:
                            best = score[ni][nj]
                            count = ways[ni][nj]

                        elif score[ni][nj] == best:
                            count = (count + ways[ni][nj]) % MOD

                # No valid path reaches this cell
                if best == -1:
                    continue

                # Add current cell's value (ignore E and S)
                if board[i][j] in ('E', 'S'):
                    value = 0
                else:
                    value = int(board[i][j])

                score[i][j] = best + value
                ways[i][j] = count

        if ways[0][0] == 0:
            return [0, 0]

        return [score[0][0], ways[0][0]]
    
#Input: board = ["E23","2X2","12S"]
#Output: [7,1]
