def knutt_morris_prath(text, pattern):
    n, m = len(text), len(pattern)
    indices = []
    if n < m :
        return indices
    i = 0 #index for text
    j = 0 #index for pattern
    lps = compute_prefix_function(pattern, m)
    while i < n :
        if pattern[j] == text[i]:
            i+=1
            j+=1
        if j == m :#pattern found :
            indices.append(i-m+1)
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]: #mismatch
            if j > 0 : #pattern[j-1] was matching => keep searching
                j = lps[j-1]
            else:
                i+=1
    return indices


def compute_prefix_function(pattern, m):
   k = 0 #longest prefix seen so far
   lps = [0]*m
   for i in range(1,m):
       if pattern[i] == pattern[k]:
           k+=1
           lps[i] = k
       else:
           if k != 0 :
               k = lps[k-1]
   return lps

if __name__ == "__main__":
    text = "abdababaaabadbababaaa"
    pattern = "ababaaa"
    print knutt_morris_prath(text, pattern)


