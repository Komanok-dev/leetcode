import collections


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        result, dq = float("-inf"), collections.deque()
        for i in range(len(nums)):
            if dq and i-dq[0][0] == k+1:
                dq.popleft()
            curr = nums[i] + (dq[0][1] if dq else 0)
            while dq and dq[-1][1] <= curr:
                dq.pop()
            if curr > 0:
                dq.append((i, curr))
            result = max(result, curr)
        return result
