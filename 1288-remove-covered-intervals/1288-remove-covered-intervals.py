
class Solution(object):
    def removeCoveredIntervals(self, intervals):

        # Step 1: Sort intervals
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        right = 0

        # Step 2: Traverse intervals
        for start, end in intervals:

            # Check if interval is not covered
            if end > right:
                count += 1
                right = end

        return count
