import heapq

class Vertice :
    def __init__(self, val):
        self.node = val
        self.dist = 10**9

    def __hash__(self):
        return hash(self.node)

    def __eq__(self, other):
        return self.node == other.node

    def __str__(self):
        return "(" + str(self.node) + "," + str(self.dist) + ")"

class PriorityQueue :
    def __init__(self, heap=[]):
        heapq.heapify(heap)
        self.heap = heap
        self.node_finder = {el[-1]: el for el in self.heap}
        self.REMOVED = "<ENTRY REMOVED>"

    def insert(self, node, priority=0):
        if node in self.node_finder :
            self.delete(node)
        entry = [priority, node]
        self.node_finder[node] = entry
        heapq.heappush(self.heap, entry)

    def delete(self,node):
        if node in self.node_finder :
            entry = self.node_finder.pop(node)
            entry[-1] = self.REMOVED

    def pop(self):
        while self.heap :
            priority, node = heapq.heappop(self.heap)
            if node != self.REMOVED :
                del self.node_finder[node]
                return priority, node
        return None

    def printHeap(self):
        for el in self.heap :
            print el[0], el[-1]
        print ""

    def isNotEmpty(self):
        return self.node_finder != {}

if __name__ == "__main__":
    N = 5
    pq = PriorityQueue()
    for v in range(1,N+1):
        pq.insert(v, 10**9)
    pq.insert(2)
    pq.insert(3,2)
    pq.insert(4,1)
    while pq.isNotEmpty() :
        el = pq.pop()
        if el != pq.REMOVED :
            print(el)


