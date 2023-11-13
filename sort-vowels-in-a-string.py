class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        letters = []
        idx = []
        s = list(s)
        for i, c in enumerate(s):
            if c in vowels:
                letters.append(c)
                idx.append(i)
        letters.sort()
        for i, c in zip(idx, letters):
            s[i] = c
        return ''.join(s)
