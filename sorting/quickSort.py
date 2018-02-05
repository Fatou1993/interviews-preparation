import random

def quickSortRec(arr, left, right):
    if left < right :
        #print(arr[left:(right+1)])
        q = partition(arr, left, right)
        quickSortRec(arr, left, q-1)
        quickSortRec(arr, q+1, right)

def quickSort(arr):
    quickSortRec(arr, 0, len(arr)-1)

def partition(arr, left, right):
    #r = random.randint(left, right)
    #arr[r], arr[right] = arr[right], arr[r]
    pivot = arr[right]
    smaller = left-1
    for i in range(left, right):
        if arr[i] < pivot :
            smaller += 1
            arr[i], arr[smaller] = arr[smaller], arr[i]
    smaller+=1
    arr[smaller], arr[right] = arr[right], arr[smaller]
    return smaller

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    #print(arr)
    quickSort(arr)
    partition(arr, 0, len(arr)-1)
    print arr

