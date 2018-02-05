def power(x,y):
    if y == 1 :
        return x
    elif y == 0 :
        return 1
    if y < 0 :
        x, y = 1.0/x, -y
    tmp = power(x,y>>1)
    if x&1 :
        return tmp*tmp*x
    return tmp*tmp

if __name__ == "__main__":
    x, y = 100, 2
    print power(x,y)