class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count = 0
        for sentence in sentences:
            count = max(count, sentence.count(' '))
        return count + 1
