class MinHeap :
    def __init__(self):
        self.elements = []
        self.num_elements = 0

    def insert(self, x):
        self.elements.append(x)
        idx_new_element = self.num_elements
        self.num_elements += 1
        self.heapifyUp(idx_new_element)

    def remove(self, x):
        idx_element_to_remove = self.find(x)
        if idx_element_to_remove != - 1 : #element present
            element_removed = self.elements[idx_element_to_remove]
            self.elements[idx_element_to_remove] = self.elements[-1] #replace by last element
            self.elements.pop()
            self.num_elements-=1
            self.heapifyDown(idx_element_to_remove)
            return element_removed
        return None

    def find(self, x):
        return self.find_helper(0, x)

    def find_helper(self, idx, x):
        if idx >= self.num_elements or self.elements[idx] < x :
            return -1
        if self.elements[idx] == x :
            return idx
        left_child_idx = 2*idx+1
        lookInLeft = self.find_helper(left_child_idx, x)
        if lookInLeft != -1:
            return lookInLeft
        right_child_idx = 2 * idx + 2
        return self.find_helper(right_child_idx, x)


    def getMin(self):
        if self.num_elements :
            return self.remove(self.elements[0])
        raise IndexError('empty heap')

    def heapifyUp(self, idx):
        while idx > 0 and self.elements[(idx-1)/2] > self.elements[idx]:
            self.elements[(idx-1)/2], self.elements[idx] = self.elements[idx], self.elements[(idx-1)/2]
            idx = (idx-1)/2

    def heapifyDown(self, idx):
        if idx >= self.num_elements :
            return
        smaller = idx
        left_child_idx = 2*idx+1
        if left_child_idx < self.num_elements and self.elements[left_child_idx] < self.elements[smaller]:
            smaller = left_child_idx
        right_child_idx = 2 * idx + 2
        if right_child_idx < self.num_elements and self.elements[right_child_idx] < self.elements[smaller]:
            smaller = right_child_idx
        if smaller != idx : #element need to be moved
            self.elements[smaller], self.elements[idx] = self.elements[idx], self.elements[smaller]
            self.heapifyDown(smaller)

    def isEmpty(self):
        return self.num_elements == 0


if __name__ == "__main__":
    arr = [2,3,5,1,8,6,13,0,4]
    min_heap = MinHeap()
    for x in arr :
        min_heap.insert(x)
        #print min_heap.elements
    while not min_heap.isEmpty():
        print min_heap.getMin(),

