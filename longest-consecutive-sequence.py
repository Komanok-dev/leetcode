class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()
        print(nums)
        longest, streak = 1, 1
        for i in range(1, len(nums)):
            print(nums[i])
            if nums[i] - nums[i-1] == 1:
                streak += 1
            elif nums[i] - nums[i-1] > 1:
                longest = max(longest, streak)
                streak = 1
        longest = max(longest, streak)
        return longest
