class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for _ in range(1, n+1):
            third = first + second
            first = second
            second = third
        return second
