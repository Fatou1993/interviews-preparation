class TreeNode:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def preorder(self):
        self.preOrder(self.root)

    def preOrder(self, root):
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postorder(self):
        self.postOrder(self.root)

    def postOrder(self, root):
        if root:
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(root.data)

class Solution(object):
    def getPath(self, root, p, path):
        if not root:
            return path
        if root == p:
            path.append(p)
            return path
        path.append(root)
        left_path = self.getPath(root.left, p, path)
        if left_path and left_path[-1] == p:
            return path
        right_path = self.getPath(root.right, p, path)
        if right_path and right_path[-1] == p:
            return path
        path.pop()
        return path

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        elif p == root or q == root:
            return root
        path_p = self.getPath(root, p, [])
        len_p = len(path_p)
        path_q = self.getPath(root, q, [])
        len_q = len(path_q)
        for i in range(min(len_p, len_q)):
            u, v = path_p[i], path_q[i]
            if u != v:
                return path_p[i - 1]
        return p if len_p < len_q else q

if __name__ == "__main__":
    #arr = [-1,0,3,-2,4,None,None,8]
    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(8)
    tree = Tree(root)
    s = Solution()
    print s.lowestCommonAncestor(root, root.left.left.left, root.left)



