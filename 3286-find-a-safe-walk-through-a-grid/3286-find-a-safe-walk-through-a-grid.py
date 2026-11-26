
from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        # Check starting cell
        health -= grid[0][0]

        if health <= 0:
            return False

        # Store maximum remaining health at each cell
        best = [[0] * n for _ in range(m)]
        best[0][0] = health

        q = deque([(0, 0, health)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, h = q.popleft()

            # Destination reached
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    nh = h - grid[nr][nc]

                    if nh > 0 and nh > best[nr][nc]:

                        best[nr][nc] = nh
                        q.append((nr, nc, nh))

        return False
