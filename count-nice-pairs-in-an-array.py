class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        counter = 0
        cache = {}
        for i in range(len(nums)):
            temp = nums[i]
            rev_i = 0
            while temp:
                rev_i = rev_i * 10 + temp % 10
                temp //= 10
            counter += cache.get(nums[i]-rev_i, 0)
            cache[nums[i]-rev_i] = cache.get(nums[i]-rev_i, 0) + 1
        return counter % MOD
