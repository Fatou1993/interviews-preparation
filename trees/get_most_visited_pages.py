import bintrees

def get_most_visited_pages(it, k):
    next_page = next(it, None)
    rbt = bintrees.RBTree()
    num_elements = 0
    while next_page :
        if next_page in rbt :
            rbt[next_page] += 1
        else :
            if num_elements == k :
                rbt.min_key() #remove the min key
            else:
                rbt[next_page] = 1
                num_elements+=1
        next_page = next(it, None)
    return rbt

if __name__ == "__main__":
    pages = ["g","a","t","t","a","a","a","g","t","c"]
    it = iter(pages)
    res = get_most_visited_pages(it, 2)
    print res

