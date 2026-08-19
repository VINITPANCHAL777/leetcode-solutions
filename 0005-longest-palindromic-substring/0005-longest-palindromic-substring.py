class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, max_len = 0, 1  # track best palindrome found so far

        def expand_around_center(left: int, right: int) -> int:
            # Expand outward while characters match; return length of palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # actual palindrome length

        for i in range(len(s)):
            # Odd-length palindrome (single character center)
            len1 = expand_around_center(i, i)
            # Even-length palindrome (between i and i+1)
            len2 = expand_around_center(i, i + 1)

            curr_max = max(len1, len2)
            if curr_max > max_len:
                max_len = curr_max
                # Recompute start index of this palindrome
                start = i - (curr_max - 1) // 2

        return s[start:start + max_len]