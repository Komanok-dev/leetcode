class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            hash.add(num)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if hash.get(num):
                return True
            else:
                hash[num] = 1

    def containsDuplicate3(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True

    def containsDuplicate4(self, nums: List[int]) -> bool:
        nums.sort()
        for num in range(len(nums) - 1):
            if nums[num] == nums[num+1]:
                return True
        return False
