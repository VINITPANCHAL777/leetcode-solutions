class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # the only case that overflows
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        q = 0
        for shift in range(31, -1, -1):
            if (a >> shift) >= b:      # b * 2^shift fits into what's left of a
                a -= b << shift
                q += 1 << shift

        return -q if negative else q