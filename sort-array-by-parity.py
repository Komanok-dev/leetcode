class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums

    def sortArrayByParity2(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
        return nums
