class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for x, y in zip(nums[:n], nums[n:]):
            result += [x, y]
        return result
