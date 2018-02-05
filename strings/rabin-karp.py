"""
Take away : don't forget the modulo
Compare with the last text
Be careful with the first indice
"""

def getHash(c):
    return ord(c)-ord('a')

def rabinkarp(text, pattern):
    """
    Return the index where pattern appears in the text
    :param text:
    :param pattern:
    :return:
    """
    n = len(text)
    m = len(pattern)
    res = []
    if n < m :
        return res
    #compute hash
    q = 11 #prime number used
    d = 26 #size of our alphabet
    h = (10**(m-1))%q

    p_h = t_h = 0
    for i in range(m):
        p_h = (p_h*d+getHash(pattern[i]))%q
        t_h = (t_h*d+getHash(text[i]))%q

    for i in range(m, n):
        if p_h == t_h and pattern == text[i-m:i]:
            res.append(i-m)
        t_h = (d*(t_h - getHash(text[i-m])*h)+getHash(text[i]))%q
    if t_h == p_h and text[n-m:n] == pattern :
        res.append(n-m)
    return res

if __name__ == "__main__":
    text = "THIS IS A TEST TEXT"
    pattern = "TEST"
    print rabinkarp(text, pattern)
