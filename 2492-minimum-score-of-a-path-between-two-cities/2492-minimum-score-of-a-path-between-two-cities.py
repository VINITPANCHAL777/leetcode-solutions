
from collections import deque

class Solution(object):
    def minScore(self, n, roads):

        # Step 1: Create adjacency list
        adj = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Step 2: BFS initialization
        q = deque([1])
        visited = set([1])

        ans = float('inf')

        # Step 3: BFS traversal
        while q:
            node = q.popleft()

            for nei, dist in adj[node]:

                # Find minimum road distance
                ans = min(ans, dist)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans
