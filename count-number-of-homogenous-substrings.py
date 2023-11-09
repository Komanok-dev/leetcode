class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        temp = s[0]
        for i in range(1, len(s)):
            if s[i] == temp[-1]:
                temp += s[i]
            else:
                if len(temp) != 1:
                    result += len(temp) * (len(temp) + 1) / 2
                else:
                    result += 1
                temp = s[i]
        result += len(temp) * (len(temp) + 1) / 2 if len(temp) != 1 else 1
        return int(result) % MOD
