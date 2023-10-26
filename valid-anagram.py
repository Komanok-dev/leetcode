from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        for key in hashS:
            if hashS[key] != hashT.get(key, 0):
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for i in s:
            hash[i] = hash.get(i, 0) + 1
        for k,v in hash.items():
            if t.count(k) < v:
                return False
        return True

    def isAnagram4(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
