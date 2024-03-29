class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            P = [0] * len(s)
            C, R = 0, 0
            for i in range(1, len(s) - 1):
                i_mirror = 2 * C - i
                if R > i:
                    P[i] = min(R - i, P[i_mirror])
                while s[i+1+P[i]] == s[i-1-P[i]]:
                    P[i] += 1
                if i + P[i] > R:
                    C, R = i, i + P[i]
            return P
        return sum((max_len + 1) // 2 for max_len in manacher(s))
