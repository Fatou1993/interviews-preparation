class TreeNode:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

class Tree :
    def __init__(self):
        self.root = None

    def preorder(self):
        self.preOrder(self.root)

    def preOrder(self, root):
        if root :
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postorder(self):
        self.postOrder(self.root)

    def postOrder(self, root):
        if root :
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(root.data)


