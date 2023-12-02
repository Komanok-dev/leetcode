from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        result = 0
        hash_chars = Counter(chars)
        for word in words:
            check = True
            hash_word = Counter(word)
            for k, v, in hash_word.items():
                if v > hash_chars.get(k, 0):
                    check = False
                    break
            if check:
                result += len(word) 
        return result
