def multiply(x, y):
    running_sum = 0
    while x :
        if x&1 :
            running_sum  = add(running_sum, y)
        x, y = x>>1, y<<1
    return running_sum

def add(x, y):
    running_sum, carryin, tmp_x, tmp_y, k = 0, 0, x, y, 1
    while tmp_x or tmp_y  :
        xk, yk = x&k, y&k
        carryout = (xk&yk)|(xk&carryin)|(yk&carryin)
        running_sum |= xk^yk^carryin
        tmp_x, tmp_y, carryin, k = tmp_x>>1, tmp_y>>1, carryout<<1, k<<1

    return running_sum | carryin
