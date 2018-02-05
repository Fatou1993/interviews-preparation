class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printRoot(self):
        if self.val:
            print self.val,
        if self.left :
            self.left.printRoot()
        if self.right:
            self.right.printRoot()

def getLeaves(root):
    #print(root.val if root else "")
    if not root :
        return []
    if not root.left and not root.right :
        leaves = [root]
    else:
        left_leaves = getLeaves(root.left)
        right_leaves = getLeaves(root.right)
        leaves = left_leaves+right_leaves
    #print("Hi", root.val, leaves)
    return leaves

def getExterior(root):
    if not root :
        return None
    left_side = [root]
    node = root.left
    while node :
        left_side.append(node)
        node = node.left
    leaves = getLeaves(root)
    right_side = []
    node = root.right
    while node :
        right_side.append(node)
        node = node.right
    return left_side + leaves[1:-1] + right_side[::-1]

if __name__ == "__main__":
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.left.left = TreeNode("C", TreeNode("D"), TreeNode("E"))
    root.left.right = TreeNode("F", None, TreeNode("G", TreeNode("H")))
    root.right = TreeNode("I")
    root.right.left = TreeNode("J", None, TreeNode("K", TreeNode("L", None, TreeNode("M")), TreeNode("N")))
    root.right.right = TreeNode("O", None, TreeNode("P"))
    root.printRoot()
    print ""
    ext = getExterior(root)
    for e in ext :
        print e.val,



