class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in reversed(range(1, len(pref))):
            pref[i] ^= pref[i-1]
        return pref
