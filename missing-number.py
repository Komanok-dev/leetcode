class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return int((len(nums)*(len(nums)+1)/2) - sum(nums))


nums = [9,6,4,2,3,5,7,0,1]
a = Solution()
print(a.missingNumber(nums))
