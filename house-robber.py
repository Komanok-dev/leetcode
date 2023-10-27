class Solution:
    def rob(self, nums: list[int]) -> int:
        one, two = 0, 0
        for n in (nums):
            temp = max(one + n, two)
            one = two
            two = temp
        return temp
