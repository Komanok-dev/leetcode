class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        poisoned = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            poisoned -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return poisoned

    def findPoisonedDuration2(self, timeSeries: list[int], duration: int) -> int:
        poisoned = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration >= timeSeries[i+1]:
                poisoned += (timeSeries[i+1] - timeSeries[i])
            else:
                poisoned += duration
        return poisoned + duration
