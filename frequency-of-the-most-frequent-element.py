class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1
        return right - left + 1
