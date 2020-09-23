from math import ceil


class HashTable:
    """
    A hash table for (key, value) 2-tuples

    === Attributes ===
    @param int capacity: total slots available
    @param list[list[tuple]] table: contents of table
    @param int collisions: number of collisions
    @param int items: number of items
    """

    def __init__(self, capacity):
        """
        Create a hash table with capacity slots

        @param HashTable self: this hash table
        @param int capacity: number of slots in this table
        @rtype: None
        """
        self.capacity, self.collisions, self.items = capacity, 0, 0
        self.table = [[] for _ in range(self.capacity)]

    def __contains__(self, value):
        """ Return whether HashTable self contains value"

        @param HashTable self: this hash table
        @param object value: value to search for
        @rtype: bool
        """
        bucket = self.table[hash(value) % self.capacity]
        return value in [item[0] for item in bucket]

    def double(self):
        """
        Double the capacity of this hash table, and re-hash all items.

        @param HashTable self: this hash table
        @rtype: None
        """
        # stats before doubling
        # print("Stats before doubling: {}".format(self.stats()))
        # temporarily save self.table
        tmp_table = self.table
        self.capacity *= 2
        self.items = 0
        self.table = [[] for _ in range(self.capacity)]
        # insert items into new table
        for bucket in tmp_table:
            for item in bucket:
                self.insert(item)
        # stats after doubling
        # print("Stats after doubling: {}".format(self.stats()))

    def insert(self, item):
        """
        Insert (key, value) item into HashTable self.

        @param HashTable self: this HashTable
        @param (object, object) item: key/value pair, key is hashable
        @rtype: None
        """
        # find the appropriate bucket
        bucket = self.table[hash(item[0]) % self.capacity]
        # insert item if it's not there
        # update collisions if there are other items in bucket
        if not any([t[0] == item[0] for t in bucket]):
            bucket.append(item)
            self.items += 1
            if len(bucket) > 1:
                self.collisions += 1
        # overwrite value if key is already there
        else:
            for i in range(len(bucket)):
                if bucket[i][0] == item[0]:
                    bucket[i] = item
        if (self.items / self.capacity) > 0.7:
            self.double()

    def retrieve(self, key):
        """
        Return value corresponding to key, or else raise Exception.

        @param HashTable key: this hash table
        @param object key: hashable key
        @rtype: object
        """
        # use the hash to get the right bucket
        bucket = self.table[hash(key) % self.capacity]
        # use the key to get the right item in bucket
        # but complain if key is absent
        for item in bucket:
            if key == item[0]:
                return item[1]
        # raise an error if key not present
        raise KeyError("{}".format(key))

    def stats(self):
        """
        Provide statistics.

        @param HashTable self: this hash table
        @rtype: str
        """
        buckets = sum([1 for b in self.table if len(b) > 0])
        average = "Average bucket length: {}\n".format(self.items / buckets)
        ideal = "Ideal bucket length: {}".format(
            round(ceil(self.items / self.capacity)))
        return average + ideal


if __name__ == '__main__':
    import random

    word_list = open('words.txt').readlines()
    random.shuffle(word_list)
    ht = HashTable(2)
    for j in range(354983):
        ht.insert((word_list[j], hash(word_list[j])))
    print(ht.stats())
    print('and\n' in ht)
    print('the\n' in ht)
    print('centre\n' in ht)

    print(ht.capacity)
    print(hash("centre\n"))
    print(hash("centre\n") % ht.capacity)
    print(ht.retrieve("centre\n"))
