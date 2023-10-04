class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ''
        for c in s:
            result += chr(ord(c) + 32) if 'A' <= c <= 'Z' else c
        return result
