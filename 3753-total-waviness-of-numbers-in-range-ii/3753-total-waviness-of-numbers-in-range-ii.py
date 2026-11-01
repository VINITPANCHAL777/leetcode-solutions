class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def f(n):
            if n <= 0:
                return 0
            digits = [int(c) for c in str(n)]
            L = len(digits)
            memo = {}

            def dfs(pos, p2, p1, tight, started):
                if pos == L:
                    return (1, 0)
                key = (pos, p2, p1, tight, started)
                if key in memo:
                    return memo[key]
                limit = digits[pos] if tight else 9
                cnt = 0
                total = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    gain = 0
                    if not started and d == 0:
                        c, s = dfs(pos + 1, -1, -1, ntight, False)
                    elif not started:
                        c, s = dfs(pos + 1, -1, d, ntight, True)
                    else:
                        if p2 != -1:
                            if (p1 > p2 and p1 > d) or (p1 < p2 and p1 < d):
                                gain = 1
                        c, s = dfs(pos + 1, p1, d, ntight, True)
                    cnt += c
                    total += s + gain * c
                memo[key] = (cnt, total)
                return memo[key]

            return dfs(0, -1, -1, True, False)[1]

        return f(num2) - f(num1 - 1)