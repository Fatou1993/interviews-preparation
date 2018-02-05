def parity(x):
    """
    parity = number of 1s % 2
    """
    parity = 0
    while x :
        parity ^= x&1
        x = x&(x-1) #unset lowest 1 bit
    return parity


def parity_using_precomputed_values(x, precomputed_parities):
    MASK_SIZE = 16
    MASK = 0xFFFF
    return precomputed_parities[x&MASK] ^ precomputed_parities[(x>>MASK_SIZE)&MASK] \
           ^ precomputed_parities[(x>>2*MASK_SIZE)&MASK] ^ precomputed_parities[(x>>3*MASK_SIZE)]


def parity_using_associativity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

