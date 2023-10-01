import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()
    
    def isPowerOfThree2(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        if n == 1:
            return True
