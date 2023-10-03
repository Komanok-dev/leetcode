class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count = 0
        for x, y in zip(startTime, endTime):
            if x <= queryTime <= y:
                count += 1
        return count
