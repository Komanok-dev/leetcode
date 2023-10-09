class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
             return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = right = mid
                while left > 0 and nums[left-1] == target:
                        left -= 1
                while right < len(nums)-1 and nums[right+1] == target:
                        right += 1
                return [left, right]
        return [-1, -1]
