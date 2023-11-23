class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        def check_diff(left, right):
            arr = sorted(nums[left:right+1])
            if len(arr) == 1:
                return True
            diff = arr[1] - arr[0]
            for i, j in zip(arr, arr[1:]):
                if (abs(i - j)) != diff:
                    return False
            return True

        result = []
        for left, right in zip(l, r):
            result.append(check_diff(left, right))
        return result
