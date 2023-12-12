class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

    def maxProduct2(self, nums: list[int]) -> int:
        num1 = num2 = 0
        for num in nums:
            if num > num1:
                num1, num2 = num, num1
            elif num > num2:
                num2 = num
        return (num1 - 1) * (num2 - 1)
