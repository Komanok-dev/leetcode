from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        dupl, miss = 0, 0
        for i in range(1, len(nums) + 1):
            if counter[i] == 2:
                dupl = i
            if counter[i] == 0:
                miss = i
        return [dupl, miss]
