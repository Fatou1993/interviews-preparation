import heapq

def getMinIndex(cands, n):
    minE = min(cands)
    return next((i for i in range(n) if cands[i] == minE), n)


def getMaxIndex(cands, n):
    maxE = max(cands)
    return next((i for i in range(n) if cands[i] == maxE), n)

def find_closest_elements_in_sorted_arrays(sorted_arrays):
    """
    Get the closest elements in array
    :param sorted_arrays:
    :return:
    """
    n = len(sorted_arrays)
    res = []
    if not n : return res
    min_heap = []
    cands = [None] * n
    for i, arr in enumerate(sorted_arrays) :
        heapq.heappush(min_heap, (arr[0],i, 0))
        cands[i] = arr[0]
        arr.append(float("inf")) #to get more easy loop

    num_elements_set = n
    min_interval = float("inf")

    while min_heap[0][0] != float("inf"):
        if num_elements_set == n:  # all arrays have a representative
            print "cands:", cands
            minIdx, maxIdx = getMinIndex(cands, n), getMaxIndex(cands, n)
            interval = cands[maxIdx] - cands[minIdx]
            if interval < min_interval:
                res = list(cands)
                min_interval = interval
            cands[minIdx] = None  # suppress smaller element
            num_elements_set -= 1
        else :
            print "min_heap:", min_heap
            el, array_index, idx = heapq.heappop(min_heap) #get min element then add the next element in the same array
            next_element = (sorted_arrays[array_index][idx+1], array_index, idx+1)
            heapq.heappush(min_heap, next_element)
            if cands[array_index] is None : #it is the first time the array_index th is seen
                cands[array_index] = el
                num_elements_set += 1
            else: #replace element in sorted_arrays[i] by most recent value
                    cands[array_index] = el
    return res

if __name__ == "__main__":
    sorted_arrays = [[5,10,15],[3,6,9,12,15],[8,16,24]]
    res = find_closest_elements_in_sorted_arrays(sorted_arrays)
    print res

