import heapq
import itertools
def sort_approximately_sorted_arrays(sequence, k):
    min_heap = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence[k:]:
        smallest = heapq.heappushpop(min_heap, x)
        print smallest,

    while min_heap :
        smallest = heapq.heappop(min_heap)
        print smallest,

    return

if __name__ == "__main__":
    sequence = [3,-1,2,6,4,5,8]
    k = 2
    sort_approximately_sorted_arrays(sequence, k)