class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                result[stack_idx] = i - stack_idx
            stack.append(i)
        return result
