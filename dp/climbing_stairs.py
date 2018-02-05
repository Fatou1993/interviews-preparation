def climbing_stairs(top, maximum_step):
    def compute_number_of_ways_to_h(h):
        if h <= 1 :
            return 1
        if number_of_ways_to_h[h] == 0 :
            number_of_ways_to_h[h] = sum(compute_number_of_ways_to_h(h-i) for i in range(1,min(maximum_step,h)+1))
        return number_of_ways_to_h[h]

    number_of_ways_to_h  = [0]*(top+1)
    return compute_number_of_ways_to_h(top)

if __name__ == "__main__":
    top, maximum_step = 4, 2
    print climbing_stairs(top, maximum_step)