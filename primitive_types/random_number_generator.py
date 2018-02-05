import random
def random_number_generator(lower_bound, upper_bound):
    number_elements = upper_bound-lower_bound+1
    while True :
        result, i = 0, 0
        while (1<<i) < number_elements :
            result = (result << 1) | random.randint(0,1)
            i+=1
        if result < number_elements :
            break
    return result+lower_bound

if __name__ == "__main__" :
     lower_bound, upper_bound = 4, 17
     print random_number_generator(lower_bound, upper_bound)

