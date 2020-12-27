""" Our own hash table """


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

    def __contains__(self, item):
        """ Return whether HashTable self contains item"

        @param HashTable self: this hash table
        @param tuple item: item to search for
        @rtype: bool
        """
        # can use the key to find the bucket, then hopefully not too many
        # things in the bucket (ie not too many collisions)
        bucket_to_check = hash(item[0]) % self.capacity
        bucket = self.table[bucket_to_check]
        return item in bucket

    def contains_value(self, value):
        """ Return whether HashTable self contains a pair with value value"

        @param HashTable self: this hash table
        @param object value: value to search for
        @rtype: bool
        """
        # which bucket to look in? we can't tell!
        # have to look at all items
        for bucket in self.table:
            for item in bucket:
                if item[1] == value:
                    return True
        return False

    def double(self):
        """
        Double the capacity of this hash table, and re-hash all items.

        @param HashTable self: this hash table
        @rtype: None
        """
        temp = self.table
        # double size of our table
        self.items = 0
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        # re-insert all the items
        for bucket in temp:
            for item in bucket:
                self.insert(item)

    def insert(self, item):
        """
        Insert (key, value) item into HashTable self.
        #key: yao bei hash obj, value: already hashed value

        @param HashTable self: this HashTable
        @param (object, object) item: key/value pair, key is hashable
        @rtype: None
        """
        # determine which bucket it should go in
        index_to_check = hash(item[0]) % self.capacity
        bucket = self.table[index_to_check]
        # if not in hash table, add it
        if item not in bucket:
            bucket.append(item)
            self.items += 1
            if len(bucket) > 1:
                self.collisions += 1
        # check if we need to grow the table
        if (self.items / self.capacity) > 0.66:
            self.double()

    def retrieve(self, key):
        """
        Return value corresponding to key, or else raise Exception.

        @param HashTable key: this hash table
        @param object key: hashable key
        @rtype: object
        """
        # find the right bucket
        index_to_check = hash(key) % self.capacity
        bucket = self.table[index_to_check]
        # get the first item matching key from bucket
        for item in bucket:
            if item[0] == key:
                return item[1]
        # raise an error if key is not in hash table
        raise KeyError('{} not in hash table'.format(key))

    def stats(self):
        """
        Provide statistics.

        @param HashTable self: this hash table
        @rtype: str
        """
        buckets = sum([1 for b in self.table if len(b) > 0])
        average = "Average bucket length: {}.\n".format(self.items / buckets)
        ideal = "Density: {}\n".format(self.items / self.capacity)
        collisions = "Collisions: {}".format(self.collisions)
        return average + ideal + collisions


if __name__ == '__main__':
    import random
    word_list = [line.strip().lower() for line in open('/usr/share/dict/words')]
    random.shuffle(word_list)
    ht = HashTable(20)
    for j in range(100000):
        ht.insert((word_list[j], hash(word_list[j])))
    print(ht.stats())
    print(('and', hash('and')) in ht)
    print(ht.retrieve('the'))
    # print(ht.retrieve('bananaphone'))
