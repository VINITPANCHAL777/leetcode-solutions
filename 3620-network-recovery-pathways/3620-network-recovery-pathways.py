
from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        adj = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        # Build graph
        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            costs.append(w)

        # Step 1: Topological Sorting
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, w in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # Step 2: Check whether a given score is possible
        def canReach(limit):
            INF = float('inf')

            dist = [INF] * n
            dist[0] = 0

            for u in topo:

                if dist[u] == INF or not online[u]:
                    continue

                for v, w in adj[u]:

                    if not online[v] or w < limit:
                        continue

                    new_cost = dist[u] + w

                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        # Step 3: Binary Search
        if not costs:
            return -1

        costs = sorted(set(costs))

        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if canReach(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans
