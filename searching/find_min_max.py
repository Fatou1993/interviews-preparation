from collections import namedtuple

def find_min_max(A) :
    MinMax = namedtuple("MinMax", ("smallest", "largest"))

    def min_max(a,b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    n = len(A)
    if n <= 1 :
        return MinMax(A[0],A[0])
    global_min_max = min_max(A[0],A[1])
    for i in range(2, n-1, 2):
        local_min_max = min_max(A[i], A[i+1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest)
        )
    if n%2 : #odd number of elements
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )
    return global_min_max