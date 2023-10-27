class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        one, two = 1, 1
        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
