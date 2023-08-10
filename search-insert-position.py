class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) < 1 or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1
        while True:
            if target <= nums[mid] and target > nums[mid-1]:
                return mid
            if target < nums[mid]:
                right = mid
                mid = (left + mid) // 2
            else:
                left = mid
                mid = (right + mid) // 2 + 1

    def searchInsert2(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
        return left
