import bisect


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        for i in [arr[len(arr)//4], arr[len(arr)//2], arr[len(arr)*3//4]]:
            if (bisect.bisect_right(arr, i) - bisect.bisect_left(arr, i)) * 4 > len(arr):
                return i
        return arr[-1]
