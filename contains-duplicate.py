class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        for num in nums:
            if hash.get(num):
                return True
            else:
                hash[num] = 1

    def containsDuplicate2(self, nums: list[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True
