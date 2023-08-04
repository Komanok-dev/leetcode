class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix = ''
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                break
            prefix += strs[0][i]
        return prefix
