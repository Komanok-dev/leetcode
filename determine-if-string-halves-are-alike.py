class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        a, b = 0, 0
        for i in range(len(s)):
            if i < len(s) // 2:
                a += s[i] in vowels
            else:
                b += s[i] in vowels
        return a == b
