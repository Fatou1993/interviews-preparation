def mergeSortRec(arr, left, right):

    if left < right :
        mid = (left+right)/2
        mergeSortRec(arr, left, mid)
        mergeSortRec(arr, mid+1, right)
        merge(arr, mid, left, right)

def merge(arr, mid, left, right):

    L = list(arr[left:(mid+1)])
    R = list(arr[(mid+1):(right+1)])
    n1, n2 = mid-left+1, right-mid
    idx1, idx2, idx = 0, 0, left

    while idx1 < n1 and idx2 < n2 :
        if L[idx1] <= R[idx2] :
            arr[idx] = L[idx1]
            idx1+=1
        else:
            arr[idx] = R[idx2]
            idx2+=1
        idx+=1

    while idx1 < n1 :
        arr[idx] = L[idx1]
        idx+=1
        idx1+=1

    while idx2 < n2:
        arr[idx] = R[idx2]
        idx+=1
        idx2+=1

def mergeSort(arr):
    left, right = 0, len(arr)-1
    mergeSortRec(arr, left, right)

if __name__ == "__main__":
    arr = map(int, "10 9 8 7 6 5 4 3 2 1".split(" "))
    mergeSort(arr)
    print arr
