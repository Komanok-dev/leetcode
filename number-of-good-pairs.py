from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = Counter(nums)
        result = 0
        for i in count.values():
            result += i * (i-1) // 2
        return result
