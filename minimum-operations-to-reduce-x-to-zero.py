class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] > x and nums[right] > x:
                return -1
