
class Solution:
    def maximumSaleItems(self, items, budget):

        n = len(items)

        # Calculate free items for every item type
        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        # Find the cheapest item
        min_idx = min(range(n), key=lambda i: items[i][1])

        min_price = items[min_idx][1]
        min_free = free[min_idx]

        # Knapsack DP for all items except the cheapest
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):

            if i == min_idx:
                continue

            factor, price = items[i]
            value = 1 + free[i]

            for b in range(budget, price - 1, -1):
                if dp[b - price] != -1:
                    dp[b] = max(dp[b], dp[b - price] + value)

        ans = 0

        # Use remaining budget to buy cheapest item
        for b in range(budget + 1):

            if dp[b] == -1:
                continue

            remaining = budget - b

            if remaining >= min_price:
                total = dp[b] + min_free + remaining // min_price
            else:
                total = dp[b]

            ans = max(ans, total)

        return ans
