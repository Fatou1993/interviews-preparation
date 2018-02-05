class Queue :
    SCALE_FACTOR = 2

    def __init__(self, initial_size):
        self.arr = [None]*initial_size
        self.size = initial_size
        self.num_elements = 0
        self.start = self.end = 0

    def enqueue(self, x):
        if self.num_elements == self.size : #array full => resize it
            self.arr = list(self.arr[self.start:]) + list(self.arr[:self.start]) + [None]*self.size*(self.SCALE_FACTOR-1)
            self.start = 0
            self.end = self.num_elements
            self.size *= self.SCALE_FACTOR
        self.arr[self.end] = x
        self.end+=1
        self.end = self.end % self.size
        self.num_elements+=1

    def dequeue(self):
        if self.num_elements == 0 : #no elements to deque
            return None
        res = self.arr[self.start]
        self.start+=1
        self.start = self.start % self.size
        self.num_elements-=1
        return res

    def numElements(self):
        return self.num_elements

    def isEmpty(self):
        return self.num_elements == 0

if __name__ == "__main__":
    q = Queue(4)
    arr = [4,5,8,9]
    for x in arr :
        q.enqueue(x)
    print q.arr
    while not q.isEmpty() :
        x = q.dequeue()
        print x,
