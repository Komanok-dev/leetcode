class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        result = right = 0
        for left in range(len(nums)):
            while right < len(nums) and nums[right] <= nums[left]+n-1:
                right += 1
            result = max(result, right-left)
        return n-result
