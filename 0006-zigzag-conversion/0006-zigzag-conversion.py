class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        currentRow = 0
        direction = 1

        for char in s:
            rows[currentRow] += char

            if currentRow == 0:
                direction = 1
            elif currentRow == numRows - 1:
                direction = -1

            currentRow += direction

        return ''.join(rows)