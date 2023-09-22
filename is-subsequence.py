class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        position = 0
        for letter in s:
            position = t.find(letter, position)
            if position == -1:
                return False
            position += 1
        return True
