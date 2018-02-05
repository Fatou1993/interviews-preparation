def replace_and_remove(arr, size):
    """
    a is replaced by 2 d
    d is removed
    size element are filled and there is enough place in the array
    Steps :
    suppress b's and compute final size
    fill the array starting with the last value
    :param arr:
    :return:
    """
    writing_index = 0
    number_of_as = 0
    for i in range(size):
        if arr[i] != 'b':
            arr[writing_index] = arr[i]
            writing_index+=1
        if arr[i] == "a":
            number_of_as += 1
    final_size = number_of_as + writing_index #final size
    writing_index -= 1 #this is the last element in the array where the b's have been removed
    while writing_index >= 0 :
        if arr[writing_index] == "a":
            arr[final_size-2:final_size] = ["d","d"]
            final_size-=2
        else:
            final_size -= 1
            arr[final_size] = arr[writing_index]
        writing_index-=1
    return arr



if __name__ == "__main__":
    arr = ["a","c",'a',"a","","",""]
    print replace_and_remove(arr,4)
