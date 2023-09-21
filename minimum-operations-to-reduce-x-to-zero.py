class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        pass




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
