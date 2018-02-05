def intersect_two_sorted_arrays(A, B):
    intersection = []
    n, m = len(A), len(B)
    i = j = 0
    while i < n and j < m:
        #print A[i], B[j], intersection
        if A[i] < B[j]:
            i+=1
        elif A[i] > B[j]:
            j+=1
        elif A[i] == B[j] :
            if not intersection or intersection[-1] != A[i]:
                intersection.append(A[i])
            i, j = i+1, j+1

    return intersection

if __name__ == "__main__":
    A = [2,3,3,5,5,6,7,7,8,12]
    B = [5,5,6,8,8,9,10,10]
    print intersect_two_sorted_arrays(A, B)