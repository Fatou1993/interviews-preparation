import bisect
def search_first_of_k_using_bisect(A, k):
    i = bisect.bisect_left(A,k)
    if i == len(A):
        return None
    return i

def search_first_of_k(A,k):
    n = len(A)
    start, end = 0, n-1
    candidate = None
    while start <= end :
        mid = (start+end)//2
        if A[mid] < k :
            start = mid +1
        else:
            if A[mid] == k :
                candidate = mid
            end = mid-1
    return candidate



if __name__ == "__main__":
    A = [-14,-10,2,108,108,243,285,285,285,401]
    print search_first_of_k_using_bisect(A,108)
    print search_first_of_k(A, 108)