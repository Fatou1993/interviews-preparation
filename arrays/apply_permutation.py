def apply_permutation(perm, A):
    n = len(A)
    for i in range(n):
        while i != perm[i]:
            print i, perm[i]
            A[i], A[perm[i]] = A[perm[i]], A[i]
            tmp = perm[perm[i]]
            perm[perm[i]] = perm[i]
            perm[i] = tmp

if __name__ == "__main__":
    A = ["a", "b", "c", "d"]
    perm = [2,0,1,3]
    apply_permutation(perm, A)
    print A
