import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_char(string):
            skip = 0
            for i in reversed(range(len(string))):
                if string[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield string[i]

        for x, y in itertools.zip_longest(next_char(s), next_char(t)):
            if x != y:
                return False
        return True
