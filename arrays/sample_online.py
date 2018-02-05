import random
def sample_online(it, k):
    sampling_results = []
    num_elements_seen_so_far = 0
    for val in it :
        if num_elements_seen_so_far < k :
            sampling_results.append(val)
            num_elements_seen_so_far += 1
        else:
            num_elements_seen_so_far += 1
            idx_to_replace = random.randrange(num_elements_seen_so_far)
            if idx_to_replace < k :
                sampling_results[idx_to_replace] = val
    return sampling_results

if __name__ == "__main__":
    it = iter([random.randint(2,56) for _ in range(20)])
    print sample_online(it, 3)
