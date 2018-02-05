from collections import namedtuple

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printRoot(self):
        if self.left :
            self.left.printRoot()
        if self.val:
            print self.val,
        if self.right:
            self.right.printRoot()



def reconstruct_from_plain_level_order(nodes):
    n  = len(nodes)
    if not n :
        return None
    for i in range(n):
        if nodes[i] :
            nodes[i] = TreeNode(nodes[i])
    for i in range(n):
        if not nodes[i] :
            continue
        left = 2*i+1
        right = 2*i+2
        if left < n :
            nodes[i].left = nodes[left]
        if right < n :
            nodes[i].right = nodes[right]
    return nodes[0]

def searchRangeInBST(root, interval):
    def searchRangeInBSTHelper(root, min_interval, max_interval):
        print res , min_interval, max_interval, root.val if root else None
        if max_interval < min_interval or not root :
            return
        if root.val < min_interval : #search in right
            searchRangeInBSTHelper(root.right, min_interval, max_interval)
        elif root.val > max_interval : #search in left
            searchRangeInBSTHelper(root.left, min_interval, max_interval)
            return
        elif min_interval <= root.val <= max_interval :
            searchRangeInBSTHelper(root.left, min_interval, root.val)
            res.append(root.val)
            searchRangeInBSTHelper(root.right, root.val, max_interval)
            return

    res = []
    searchRangeInBSTHelper(root, interval.left, interval.right)
    return res

if __name__ == "__main__":
    Interval = namedtuple("Interval", ("left", "right"))
    interval = Interval(16,31)
    arr = [19, 7, 43, 3, 11, 23, 47, 2, 5, None, 17, None, 37, None, 53, None, None, None, None, None, None, 13, None,
           None, None, 29, 41]
    root = reconstruct_from_plain_level_order(arr)
    root.printRoot()
    print searchRangeInBST(root, interval)
        
    