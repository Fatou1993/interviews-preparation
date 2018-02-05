def palindromic_substrings(s):
    def palindromic_substrings_helper(offset, partial_partition):
        if offset == n :
            palindromes.append(list(partial_partition))
        for i in range(offset+1, n+1):
            prefix = s[offset:i]
            if prefix == prefix[::-1]: #palindrome
                palindromic_substrings_helper(i, partial_partition+[prefix])

    n = len(s)
    palindromes = []
    palindromic_substrings_helper(0, [])
    return palindromes


if __name__ == "__main__":
    s = "0204451881"
    res = palindromic_substrings(s)
    print "Paliindromes substrings"
    for r in res:
        print r
