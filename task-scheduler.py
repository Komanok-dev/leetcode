from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # result = 0
        # tasks = sorted(Counter(tasks).values(), reverse=True)
        # max_cnt = tasks[0]
        # return max((max_cnt - 1) * (n + 1) + max_cnt, len(tasks))

        counter = Counter(tasks)
        _, max_count = counter.most_common(1)[0]
        return max((max_count-1) * (n+1) + max_count, len(tasks))


tasks = ["A","A","B","B","B", 'C']
tasks = ["A","A","A", "B","B","B"]

n = 3



a = Solution()
print(a.leastInterval(tasks, n))