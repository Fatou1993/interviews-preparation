class HashTable :
    def __init__(self, size=20):
        self.arr = [None]*size
        self.size = size
        self.num_elements = 0
        self.REMOVED = "<REMOVED>"

    def copyElements(self, new_arr):
        for x in self.arr :
            if x and x is not self.REMOVED :
                self.insertWhenEnoughPlace(x, new_arr)
        self.arr = new_arr

    def insertWhenEnoughPlace(self, x, arr):
        h = hash(x)
        idx = h % self.size
        while arr[idx] is not None:
            idx = (idx + 1) % self.size
        arr[idx] = x

    def doubleSize(self):
        self.size *= 2
        new_arr = [None] * self.size
        self.copyElements(new_arr)

    def insert(self, x):
        if self.num_elements == self.size :
            self.doubleSize()
        self.insertWhenEnoughPlace(x, self.arr)
        self.num_elements += 1


    def search(self, x):
        h = hash(x)
        idx = h % self.size
        trials = 0
        while self.arr[idx] is not None and self.arr[idx] != x :
            idx = (idx + 1) % self.size
            trials += 1
            if trials >= self.size :
                return (-1, None)
        return (-1, None) if idx >= self.size else (idx, self.arr[idx])

    def remove(self, x):
        idx, el = self.search(x)
        if idx != -1 :
            self.arr[idx] = self.REMOVED

if __name__ == "__main__":
    strings = ["abcdef", "bcdefa", "cdefab", "defabc", "aghd"]
    hash_table = HashTable(2)
    hash_table.insert(strings[0])
    print  hash_table.arr
    hash_table.insert(strings[1])
    print  hash_table.arr
    hash_table.insert(strings[2])
    print  hash_table.arr
    hash_table.insert(strings[3])
    print  hash_table.arr
    hash_table.insert(strings[4])
    print  hash_table.arr
    
