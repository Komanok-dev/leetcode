class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicate2(self, nums: list[int]) -> int:
        hash = {}
        for num in nums:
            if hash.get(num, None) is not None:
                return num
            hash[num] = 1
