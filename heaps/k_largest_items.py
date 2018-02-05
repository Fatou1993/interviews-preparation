import heapq
def k_largest_items(A, k):
    max_elements = []
    if k <= 0 :
        return max_elements
    n = len(A)
    if k >= n:
        return A
    max_heap = [(-A[0],0)]
    for _ in range(k):
        curr_min, idx = heapq.heappop(max_heap)
        max_elements.append(-curr_min)
        left_child_idx = 2*idx+1
        if left_child_idx < n :
            heapq.heappush(max_heap, (-A[left_child_idx], left_child_idx))
        right_child_idx = 2*idx+2
        if right_child_idx < n :
            heapq.heappush(max_heap, (-A[right_child_idx], right_child_idx))
    return max_elements

if __name__ == "__main__":
    A = [561, 314, 401, 28, 156, 359, 271, 11, 3]
    print k_largest_items(A,4)
