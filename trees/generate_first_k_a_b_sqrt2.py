import heapq
import math
from sets import Set

def generate_first_k_a_b_sqrt2(k):
    res = Set()
    min_heap = [0]
    num_elements = 0
    while num_elements < k: #O(klogk) complexity
        min_value = heapq.heappop(min_heap)
        if not min_value in res : #elemnent not already there
            res.add(min_value)
            num_elements += 1
            heapq.heappush(min_heap, min_value+1)
            heapq.heappush(min_heap, min_value+math.sqrt(2))
    return sorted(list(res))

if __name__ == "__main__":
    k = 10
    print generate_first_k_a_b_sqrt2(k)
