def reverse_bits(x, precomputed_reverses):
    MASK = 0xFFFF
    MASK_SIZE = 16
    return (precomputed_reverses[x&MASK]<<3*MASK_SIZE) | (precomputed_reverses[(x>>MASK_SIZE)&MASK]<<2*MASK_SIZE) | \
           (precomputed_reverses[(x>>2*MASK_SIZE)&MASK]<<MASK_SIZE) | (precomputed_reverses[(x>>3*MASK_SIZE)&MASK])

