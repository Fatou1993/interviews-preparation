import heapq

class Stack :
    def __init__(self):
        self.min_heap = []
        self.num_elements = 0
        self.timestamp = 0

    def push(self, x):
        heapq.heappush(self.min_heap, (-self.timestamp, x))
        self.num_elements+=1
        self.timestamp+=1

    def pop(self):
        if not self.num_elements :
            raise IndexError("Empty stack")
        p, val = heapq.heappop(self.min_heap)
        self.num_elements -= 1
        return val


    def peek(self):
        if not self.num_elements :
            raise IndexError("Empty stack")
        return self.min_heap[0][1]

    def isEmpty(self):
        return self.num_elements == 0


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7]
    stack = Stack()
    for x in arr :
        stack.push(x)
        print stack.min_heap

    while not stack.isEmpty():
        print stack.pop()




