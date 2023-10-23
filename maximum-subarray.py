class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        left = 0
        result = nums[0]
        for i in nums:
            if left < 0:
                left = 0
            left += i
            result = max(result, left)
        return result
