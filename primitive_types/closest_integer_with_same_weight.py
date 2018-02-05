def closest_integer_with_same_weight(x):
    """
    Find y such that (x-y) is minimum and y has same number of 1s as x
    :param x:
    :return:
    """
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS-1):
        if (x>>i)&1 != (x>>(i+1))&1 : #different bits
            mask = (1<<i)|(1<<(i+1))
            x |= mask
            return x

    raise ValueError("All bits are 0 or 1")

def get_lowest_set_bit(x):
    return x&~(x-1)

def get_lowest_not_set_bit(x):
    return ~x&(x+1)

def closest_integer_with_same_weight_constant_complexity(x):
    ns = get_lowest_not_set_bit(x)
    s = get_lowest_set_bit(x)
    if ns > s : #01....
        x|=ns #set the lowest not set bit
        x^=(ns>>1) #unset the bit before
    else: #10...
        x^=s #unset bit
        x|=(s>>1) #set zero bit

    return x





