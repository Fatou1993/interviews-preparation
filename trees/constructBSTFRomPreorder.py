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

def rebuild_bst_from_preorder(preorder):
    if not preorder :
        return None
    transition_point = next((i for i, a in enumerate(preorder) if a > preorder[0]), len(preorder))
    return TreeNode(
        preorder[0],
        rebuild_bst_from_preorder(preorder[1:transition_point]),
        rebuild_bst_from_preorder(preorder[transition_point:]))


if __name__ == "__main__":
    preorder = [43,23,37,29,31,41,47,53]
    root = rebuild_bst_from_preorder(preorder)
    root.printRoot()