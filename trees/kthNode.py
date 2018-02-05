class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.numNodes = 1

def get_number_nodes(root):
    if not root :
        return 0
    return root.numNodes

def getkthNode(root, k):
    numNodes = get_number_nodes(root)
    if numNodes < k or k <= 0: #k not valid
        return None
    leftNodes = get_number_nodes(root.left)
    if leftNodes + 1 == k :
        return root
    elif leftNodes + 1 > k :
        return getkthNode(root.left, k)
    else :
        return getkthNode(root.right, k-leftNodes-1)

