class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printRoot(self):
        if self.data:
            print self.data,
        if self.left :
            self.left.printRoot()
        if self.right:
            self.right.printRoot()


def reconstruct_preoder(preoder):
    def reconstruct_preoder_helper(preorder_iter):
        try :
            subtree_key = next(preorder_iter)
        except :
            return None
        left_subtree = reconstruct_preoder_helper(preorder_iter)
        right_subtree = reconstruct_preoder_helper(preorder_iter)
        return TreeNode(subtree_key, left_subtree, right_subtree)
    return reconstruct_preoder_helper(iter(preoder))

def getLeaves(root):
    #print(root.val if root else "")
    if not root :
        return []
    if not root.left and not root.right :
        leaves = [root.val]
    else:
        left_leaves = getLeaves(root.left)
        right_leaves = getLeaves(root.right)
        leaves = left_leaves+right_leaves
    #print("Hi", root.val, leaves)
    return leaves

if __name__ == "__main__":
    preorder = [1,2,4,5,3,None,None]
    root = reconstruct_preoder(preorder)
    #root = TreeNode(1)
    #root.left = TreeNode(2)
    #root.right = TreeNode(3)
    #root.left.left = TreeNode(4)
    #root.left.right = TreeNode(5)
    print getLeaves(root)



