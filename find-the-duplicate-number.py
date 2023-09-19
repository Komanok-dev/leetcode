class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]



# nums = [1,3,4,2,2]  # 2
nums = [3,1,3,4,2]  # 3

a = Solution()
print(a.findDuplicate(nums))