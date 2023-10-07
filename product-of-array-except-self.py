class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        tail = 1
        for i in range(len(nums)):
            result.append(tail)
            tail *= nums[i]
        tail = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= tail
            tail *= nums[i]
        return result
