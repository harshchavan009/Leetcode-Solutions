class MyHashSet:

    def __init__(self):
        self.data = bytearray(1000001)

    def add(self, key):
        self.data[key] = 1

    def remove(self, key):
        self.data[key] = 0

    def contains(self, key):
        return self.data[key] == 1