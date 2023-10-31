class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def popcount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result
        
        arr.sort(key=lambda x: (popcount(x), x))
        return arr
