class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        first, second, third = 0, 1, 1
        for _ in range(2, n):
            temp = first + second + third
            first = second
            second = third
            third = temp
        return third
