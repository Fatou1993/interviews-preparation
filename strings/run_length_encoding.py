def encode(s):
    res = []
    n = len(s)
    if not n :
        return ""
    count = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            count+=1
        else:
            res+=[str(count),s[i-1]]
            count = 1
    res+=[str(count),s[n-1]]
    return "".join(res)

def decode(s):
    res = []
    n = len(s)
    val = 0
    for i in range(n):
        if s[i].isdigit():
            val = val*10 + ord(s[i])-ord('0')
        else:
            res += [s[i]]*val
            val = 0

    return "".join(res)

if __name__ == "__main__":
    s = "aaaabcccaa"
    print encode(s)
    print decode("3e4f2e")