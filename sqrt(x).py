class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        high = x
        low = 0
        y = x // 2
        while low + 1 < high:
            if x == y * y:
                return y
            elif x > y * y:
                low = y
                y = (low + high) // 2
            elif x < y * y:
                high = y
                y = y // 2
        return low
