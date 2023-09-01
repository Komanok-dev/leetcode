class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        for i in range(1, n + 1):
            ans.append(ans[(i >> 1)] + (i & 1))
        return ans

    def countBits2(self, n: int) -> list[int]:
        ans = []
        for i in range(n + 1):
            temp = 0
            while i > 0:
                temp += i % 2
                i //= 2
            ans.append(temp)
        return ans
