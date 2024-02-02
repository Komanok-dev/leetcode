from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        q = deque(range(1, 9))
        print(q)
        while q:
            num = q.popleft()
            if num > high:
                continue
            print(low, num)
            if low <= num:
                result.append(num)
            if num % 10 + 1 < 10:
                q.append(num * 10 + num % 10 + 1)
        return result
