class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        first, second = 0, 1
        for _ in range(2, n + 1):
            temp = first + second
            first = second
            second = temp
        return second
