class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob1(nums: list[int]) -> int:
            one, two = 0, 0
            for n in (nums):
                temp = max(one + n, two)
                one = two
                two = temp
            return two
        return max(nums[0], rob1(nums[:-1]), rob1(nums[1:]))
