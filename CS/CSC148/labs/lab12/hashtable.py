class HashTable:

    def __init__(self, capacity):
        self.capacity, self.collisions, self.items = capacity, 0, 0
        self.table = [[] for _ in range(self.capacity)] #create bucket

    def __contains__(self, value):
        bucket = self.table[hash(value) % self.capacity]
        return value in [item[0] for item in bucket]

