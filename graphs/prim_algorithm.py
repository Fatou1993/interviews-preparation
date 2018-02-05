import random

def generatePermutation(n):
    arr = list(range(1,n+1))
    for i in range(n):
        r = random.randint(i, n-1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

class Vertice :
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def changePriority(self, newP):
        self.priority = newP

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

    def __str__(self):
        return "("+str(self.priority)+","+str(self.val)+")"

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.pos = {}
        self.length = 0

    def heapifyDown(self, i):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if left < self.length and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.length and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i :
            self.pos[self.heap[smallest].val], self.pos[self.heap[i].val] = self.pos[self.heap[i].val], self.pos[self.heap[smallest].val]
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.heapifyDown(smallest)

    def heapifyUp(self, i):
        idxParent = i/2
        while idxParent != i and self.heap[idxParent] > self.heap[i]:
            self.pos[self.heap[idxParent].val], self.pos[self.heap[i].val] = self.pos[self.heap[i].val], self.pos[self.heap[idxParent].val]
            self.heap[idxParent], self.heap[i] = self.heap[i], self.heap[idxParent]
            i = idxParent
            idxParent = i/2

    def insert(self, x):
        self.heap.append(x)
        self.pos[x.val] = self.length
        if self.length != 0 : #previous elements present
            self.heapifyUp(self.length)
        self.length += 1

    def isNotEmpty(self):
        return self.length != 0

    def getMin(self):
        if not self.length :
            return None
        res = self.heap[0]
        if self.length == 1 :
            self.heap = []
            self.pos = {}
            self.length -= 1
        else:
            l = self.heap[-1]
            # put the latest element at the top
            self.heap[0] = l
            self.pos[l.val] = 0

            #remove min element
            self.heap.pop()
            del self.pos[res.val]

            self.length -= 1
            self.heapifyDown(0)  #heapify down
        return res


    def fixPosition(self, idx):
        if idx/2 != idx and self.heap[idx] < self.heap[idx/2]: #go up
            self.heapifyUp(idx)
        else :
            self.heapifyDown(idx) #go down

    def updatePriority(self, u, newP):
        if u in self.pos :
            self.updatePriorityWithIndex(newP, self.pos[u])

    def updatePriorityWithIndex(self, newP, idx):
        if idx < self.length :
            self.heap[idx].changePriority(newP)
            self.fixPosition(idx)

    def printHeap(self):
        for el in self.heap :
            print el,
        print ""

if __name__ == "__main__":

    #arr = generatePermutation(9)
    arr = [9, 4, 2, 7, 1, 6, 5, 3, 8]
    pq = PriorityQueue()
    N = 9
    vertices = [Vertice(i+1,el) for i,el in enumerate(arr)]
    for v in vertices :
        pq.insert(v)
    pq.printHeap()
    print(pq.pos)
    print ""
    pq.updatePriority(5, 10)
    pq.printHeap()
    print(pq.pos)
    print ""
    pq.updatePriority(7, 0)
    pq.printHeap()
    print(pq.pos)





