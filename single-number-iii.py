class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        cache = {}
        for i in nums:
            cache[i] = cache.get(i, 0) + 1
        first = min(cache, key=cache.get)
        cache.pop(first)
        return [first, min(cache, key=cache.get)]
