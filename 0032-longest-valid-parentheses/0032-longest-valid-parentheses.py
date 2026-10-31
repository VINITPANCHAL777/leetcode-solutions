class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]          # index before the start of the current candidate run
        best = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)   # unmatched ')': new base for future runs
                else:
                    best = max(best, i - stack[-1])
        return best