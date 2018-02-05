def base_conversion(s, b1, b2):
    val = 0
    for c in s :
        val = b1*val + ord(c)-ord('0')
    is_negative = False
    if val < 0:
        is_negative, val = True, -val
    res = []
    while val :
        x = val%b2
        if 10 <= x <= 15 :
            res.append(chr(ord('A')+x-10))
        else:
            res.append(str(x))
        val = val/b2
    res = "".join(res[::-1])
    return "-"+res if is_negative else res

if __name__ == "__main__":
    print base_conversion("61537", 7, 13)