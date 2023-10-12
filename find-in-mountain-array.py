# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass

   def length(self) -> int:
       pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binarySearch(A, left, right, check):
            while left <= right:
                mid = left + (right-left) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        peak = binarySearch(mountain_arr, 0, mountain_arr.length()-1,
                            lambda x: mountain_arr.get(x) >= mountain_arr.get(x+1))
        left = binarySearch(mountain_arr, 0, peak,
                            lambda x: mountain_arr.get(x) >= target)
        if left <= peak and mountain_arr.get(left) == target:
            return left
        right = binarySearch(mountain_arr, peak, mountain_arr.length()-1,
                             lambda x: mountain_arr.get(x) <= target)
        if right <= mountain_arr.length()-1 and mountain_arr.get(right) == target:
            return right
        return -1
