from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = []
        hash = {}
        for num in nums:
            if hash.get(num, 0) == len(result):
                result.append([])
            result[hash.get(num, 0)].append(num)
            hash[num] = hash.get(num, 0) + 1
        return result


    def findMatrix2(self, nums: list[int]) -> list[list[int]]:
        cnt_nums = Counter(nums)
        max_element = max(cnt_nums.values())
        result = [[max(cnt_nums, key=cnt_nums.get)] for _ in range(max_element)]
        for k, v in cnt_nums.items():
            if k == result[0][0]:
                continue
            for i in range(v):
                result[i].append(k)
        return result
