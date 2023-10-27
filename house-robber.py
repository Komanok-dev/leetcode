class Solution:
    def rob(self, nums: list[int]) -> int:
        one, two = 0, 0
        for n in (nums):
            temp = max(one + n, two)
            one = two
            two = temp
        return temp


nums = [2,7,9,3,1]
nums = [1,2,3,1]
a = Solution()
print(a.rob(nums))
