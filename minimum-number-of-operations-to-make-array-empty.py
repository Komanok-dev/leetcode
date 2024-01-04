from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for k, v in cnt.items():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += (v // 3)
            else:
                res += (v // 3) + 1
        return res
