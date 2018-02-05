class DoublyLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class HashTable :
    """
    Class hastable methods :
    access element in 0(1)
    add an element in O(1) on average
    remove an element
    use a hash or key
    separate chaining used
    """
    def __init__(self, m=20):
        self.num_buckets = m
        self.buckets = [None]*(m)

    def insert(self, x):
        n = hash(x)
        bucket_number = n%self.num_buckets
        bucket = self.buckets[bucket_number]
        node = DoublyLinkedList(x)
        node.next = bucket
        if bucket :
            bucket.prev = node
        self.buckets[bucket_number] = node #insert node at the beginning of the list

    def remove(self, x):
        idx_bucket, node = self.lookUp(x)
        if node :
            if not node.prev and not node.next :
                self.buckets[idx_bucket] = None
            elif node.prev :
                node.prev.next = node.next
            elif node.next :
                node.next.prev = node.prev
        return self.buckets[idx_bucket]


    def lookUp(self, x):
        n = hash(x)
        bucket_number = n%self.num_buckets
        bucket = self.buckets[bucket_number]
        node = bucket
        idx = 0
        while node and node.val != x :
            idx+=1
            node = node.next
        return bucket_number, node

    def printHashTable(self):
        for i, b in enumerate(self.buckets) :
            print i, b



if __name__ == "__main__":
    strings = ["abcdef", "bcdefa", "cdefab" , "defabc"]
    hash_table = HashTable(20)
    for s in strings :
        hash_table.insert(s)
    #hash_table.printHashTable()
    #hash_table.printHashTable()
    i, x = hash_table.lookUp("abcdef")
    #print i, x
    hash_table.remove("abcdef")
    i, x = hash_table.lookUp("abcdef")
    print i, x













