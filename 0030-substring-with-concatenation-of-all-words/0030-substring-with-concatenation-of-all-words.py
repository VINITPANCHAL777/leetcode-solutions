class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n, m, w = len(s), len(words), len(words[0])
        total = m * w
        if n < total:
            return []

        need = {}
        for x in words:
            need[x] = need.get(x, 0) + 1

        res = []
        for off in range(w):
            left = off
            count = 0
            seen = {}
            for right in range(off, n - w + 1, w):
                word = s[right:right + w]
                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    # too many copies of this word: shrink from the left
                    while seen[word] > need[word]:
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                    # window holds exactly all the words
                    if count == m:
                        res.append(left)
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                else:
                    # not a word from the list: reset the window
                    seen = {}
                    count = 0
                    left = right + w
        return res