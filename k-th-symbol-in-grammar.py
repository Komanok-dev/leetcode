class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        left, right = 1, 2**(n-1)
        for _ in range(1, n):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 1 - curr
        return curr
