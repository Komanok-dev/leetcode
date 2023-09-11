class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 1
        for i in reversed(range(2, 2*n+1, 2)):
            result = result * i * (i-1) // 2 % MOD
        return result
