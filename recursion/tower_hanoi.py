def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_helper(num_rings, pegs, from_peg, to_peg, use_peg):
        if num_rings <= 0 :
            return
        compute_tower_hanoi_helper(num_rings-1, pegs, from_peg, use_peg, to_peg) #put n-1 in transition peg
        pegs[to_peg].append(pegs[from_peg].pop())
        print "Move from peg", from_peg, "to", to_peg
        compute_tower_hanoi_helper(num_rings - 1, pegs, use_peg, to_peg, from_peg) #put n-1 in final peg using initial peg as transition
        return
    pegs = [list(reversed(range(1,num_rings+1))),[],[]]
    for i in range(3):
        print "Peg:", pegs[i]
    compute_tower_hanoi_helper(num_rings, pegs, 0, 1, 2)
    for i in range(3):
        print "Peg:", pegs[i]
    return

if __name__ == "__main__":
    compute_tower_hanoi(6)




