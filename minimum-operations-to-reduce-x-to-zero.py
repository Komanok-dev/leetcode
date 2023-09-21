class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        curr = sum(nums)
        if curr < x:
            return -1
        left = 0
        result = float('inf')
        for right in range(len(nums)):
            curr -= nums[right]
            while curr < x and left <= right:
                curr += nums[left]
                left += 1
            if curr == x:
                result = min(left + len(nums) - right - 1, result)
        return result if result != float('inf') else -1

    def minOperations2(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        result = -1
        curr = left = 0
        for right in range(len(nums)):
            curr += nums[right]
            while left < len(nums) and curr > target:
                curr -= nums[left]
                left += 1
            if curr == target:
                result = max(result, right-left+1)
        return len(nums) - result if result != -1 else -1
