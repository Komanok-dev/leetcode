class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return "".join("01"[nums[i][i] == '0'] for i in range(len(nums)))
