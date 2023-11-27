class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        prefix, suffix = 0, sum(nums)
        result = []
        for i, num in enumerate(nums):
            suffix -= num
            result.append((i * num-prefix) + (suffix - ((len(nums)-1)-i)*num))
            prefix += num
        return result
