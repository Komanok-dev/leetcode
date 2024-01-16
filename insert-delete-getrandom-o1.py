import random


class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        check = len(self.set)
        self.set.add(val)
        return check + 1 == len(self.set)

    def remove(self, val: int) -> bool:
        try:
            self.set.remove(val)
            return True
        except KeyError:
            return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()