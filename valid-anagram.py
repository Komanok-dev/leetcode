class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for i in s:
            hash[i] = hash.get(i, 0) + 1
        for k,v in hash.items():
            if t.count(k) < v:
                return False
        return True
