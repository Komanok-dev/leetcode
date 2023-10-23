import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1

    def isPowerOfFour2(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(4)).is_integer()
