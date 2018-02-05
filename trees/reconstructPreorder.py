class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def reconstruct_preoder(preoder):
    def reconstruct_preoder_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if not subtree_key :
            return None
        left_subtree = reconstruct_preoder_helper(preorder_iter)
        right_subtree = reconstruct_preoder_helper(preorder_iter)
        return TreeNode(subtree_key, left_subtree, right_subtree)
    return reconstruct_preoder_helper(iter(preoder))
