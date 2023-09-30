class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        digit = float("-inf")
        stack = []
        for i in reversed(range(len(nums))):
            if nums[i] < digit:
                return True
            while stack and stack[-1] < nums[i]:
                digit = stack.pop()
            stack.append(nums[i])
        return False
