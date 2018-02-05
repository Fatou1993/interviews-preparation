import heapq
def merge_sorted_arrays(sorted_arrays):
    heap = []
    result = []
    for i, arr in enumerate(sorted_arrays) :
        if arr :
            it = iter(arr)
            key = next(it)
            heapq.heappush(heap, (key, it))

    while heap :
        num, it = heapq.heappop(heap)
        result.append(num)
        next_it = next(it, None)
        if next_it is not None :
            heapq.heappush(heap, (next_it, it))
    return result

if __name__ == "__main__":
    sorted_arrays = [[3,5,7],[0,6],[0,6,28]]
    print merge_sorted_arrays(sorted_arrays)



