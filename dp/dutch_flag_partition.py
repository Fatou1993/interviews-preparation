def dutch_flag_partition(pivot_index, A):
    n = len(A)
    pivot = A[pivot_index]
    smaller, larger, equal = 0, n, 0
    while equal < larger :
        print "equal", equal,
        if A[equal] == pivot :
            equal+=1
        elif A[equal] > pivot :
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
        else:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller+=1
            equal+=1
        print ", array:", A

if __name__ == "__main__":
    A = [0,1,2,0,2,1,1]
    dutch_flag_partition(2,A)
    print A

