class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        result = curr = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            result += curr
        return result
