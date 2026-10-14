import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val):
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.index_map:
            return False

        index = self.index_map[val]
        last = self.nums[-1]

        self.nums[index] = last
        self.index_map[last] = index

        self.nums.pop()
        del self.index_map[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)