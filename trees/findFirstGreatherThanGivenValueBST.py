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

def findFirstGreatherThanGivenValueBST(root, val):
    """
    Steps :
    do an inorder traversal of the root and get first element greater than value

    :param root:
    :param val:
    :return:
    """

    stack = []
    while stack or root:
        if root :
            stack.append(root)
            root = root.left #go left
        else:
            root = stack.pop() #go up
            if root.val > val :
                return root.val
            root = root.right #go down
    return None

def findKLargest(root, k):
    def findKLargetHelper(root):
        if root and counter[0] < k :
            findKLargetHelper(root.right)
            if counter[0] < k :
                res.append(root.val)
                counter[0]+=1
                findKLargetHelper(root.left)
        return

    counter = [0]
    res = []
    findKLargetHelper(root)
    return res

if __name__ == "__main__":
    #arr = [2,1,3]
    arr = [19,7,43,3,11,23,47,2,5,None,17,None,37,None,53,None,None,None,None,None,None,13,None,None,None,29,41]
    root = reconstruct_from_plain_level_order(arr)
    root.printRoot()
    print ""
    #print findFirstGreatherThanGivenValueBST(root, 1.5)
    print findKLargest(root,15)


