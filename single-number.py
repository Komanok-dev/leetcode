class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        cache = {}
        for i in nums:
            cache[i] = cache.get(i, 0) + 1
        return min(cache, key=cache.get)
