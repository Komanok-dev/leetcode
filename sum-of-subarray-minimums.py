class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        left, s1 = [0] * len(arr), []
        for i in range(len(arr)):
            count = 1
            while s1 and s1[-1][0] > arr[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([arr[i], count])

        right, s2 = [0] * len(arr), []
        for i in reversed(range(len(arr))):
            count = 1
            while s2 and s2[-1][0] >= arr[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([arr[i], count])

        return sum(a * l * r for a, l, r in zip(arr, left, right)) % MOD
