from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for one, two in zip_longest(word1, word2, fillvalue=''):
            result += one + two
        return result
