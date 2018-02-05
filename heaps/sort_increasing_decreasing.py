import heapq

def sort_increasing_decreasing(A):
    n = len(A)
    sorted_arrays = []
    starting_idx = 0
    increasing = 1
    for i in range(1, n+1):
        if i == n or (A[i] < A[i-1] and increasing) or (A[i] > A[i-1] and not increasing):
            sorted_arrays.append(A[starting_idx:i] if increasing else A[i-1:starting_idx-1:-1])
            starting_idx = i
            increasing ^= 1
    return merge_sorted_arrays(sorted_arrays)

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
    A = [57,131,493,294,221,339,418,452,442,190]
    print sort_increasing_decreasing(A)