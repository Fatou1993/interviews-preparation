def search_entry_equal_to_its_index(A):
    start, end = 0, len(A)-1
    while start <= end :
        mid = (start+end)/2
        if A[mid] == mid :
            return mid
        elif A[mid] < mid :
            start = mid + 1
        else :
            end = mid - 1
    return -1

