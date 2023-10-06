import math


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        digit = n // 3
        result = [3] * digit
        reminder = n - digit * 3
        if reminder == 1:
            result[-1] += 1
        elif reminder == 2:
            result.append(2)
        return math.prod(result)

    def integerBreak2(self, n: int) -> int:
        result = 0
        if n % 3 == 0:
            result = 3 ** (n // 3)
        elif n % 3 == 2:
            result = 3 ** (n // 3) * 2
        else:
            result = 3 ** (n // 3 - 1) * 4
        return result
