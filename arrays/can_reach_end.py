def can_reach_end(arr):
    last_index, furthest_index_so_far = len(arr)-1, 0
    i = 0
    while i <= furthest_index_so_far and furthest_index_so_far <= last_index :
        furthest_index_so_far = max(furthest_index_so_far, arr[i]+i)
        i+=1
    return furthest_index_so_far >= last_index

if __name__ == "__main__":
    A = [3,3,1,0,2,0,1]
    B = [3,2,0,0,2,0,1]
    print can_reach_end(A)
    print can_reach_end(B)