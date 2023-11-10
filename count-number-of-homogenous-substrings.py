class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        tmp = s[0]
        for i in range(1, len(s)):
            if s[i] == tmp[-1]:
                tmp += s[i]
            else:
                res += len(tmp) * (len(tmp) + 1) / 2 if len(tmp) != 1 else 1
                tmp = s[i]
        res += len(tmp) * (len(tmp) + 1) / 2 if len(tmp) != 1 else 1
        return int(res) % MOD
