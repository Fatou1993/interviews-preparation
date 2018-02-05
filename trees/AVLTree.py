class TreeNode :

    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1
        self.parent = None

    def printRoot(self):
        if self.left :
            self.left.printRoot()
        if self.val is not None:
            print self.val
        if self.right:
            self.right.printRoot()


class AVLTree :
    def __init__(self):
        self.root = None
        self.num_elements = 0

    def inorder(self):
        if not self.root :
            print ""
            return
        self.root.printRoot()
        print ""

    def insert(self, key):
        self.root = self.insertRec(self.root, key)

    def delete(self, key):
        self.root = self.deleteRec(self.root, key)

    def insertRec(self, root, key):
        if not root :
            return TreeNode(key)
        elif root.val == key : #no duplicate allowed
            return root
        elif root.val < key :
            root.right = self.insertRec(root.right, key)
        else:
            root.left = self.insertRec(root.left, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) #update height

        balance = self.getBalance(root) #get balance

        if balance > 1 and root.left.val > key : #left left case
            return self.rightRotate(root)

        if balance > 1 and root.left.val < key : #left right case
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and root.right.val < key : #right right case
            return self.leftRotate(root)

        if balance < -1 and root.right.val > key : #right left case
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getMinimum(self, node):
        while node and node.left :
            node = node.left
        return node

    def deleteRec(self, root, key):
        if not root :
            return root
        if root.val < key :
            root.right = self.deleteRec(root.right, key)
        elif root.val > key :
            root.left = self.deleteRec(root.left, key)
        else :
            if not root.left :
                return root.right
            elif not root.right :
                return root.left
            else:
                tmp = self.getMinimum(root.right)
                root.val = tmp.val
                root.right = self.deleteRec(root.right, tmp.val)

        if root is None :
            return root
        root.height = 1 + max(self.getHeight(root.right),self.getHeight(root.left))
        balance = self.getBalance(root)  # get balance

        if balance > 1 and self.getBalance(root.left) >= 0:  # left left case
            return self.rightRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:  # left right case
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:  # right right case
            return self.leftRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:  # right left case
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


    def rightRotate(self, node):
        left_child = node.left

        #perform rotation
        node.left = left_child.right
        left_child.right = node

        #update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        left_child.height = 1 + max(self.getHeight(left_child.left), self.getHeight(left_child.right))

        return left_child


    def leftRotate(self, node):
        right_child  = node.right

        #perform rotation
        node.right = right_child.left
        right_child.left = node

        #update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        right_child.height = 1 + max(self.getHeight(right_child.left), self.getHeight(right_child.right))

        return right_child

    def getHeight(self, root):
        if not root :
            return 0
        return root.height

    def getBalance(self, root):
        if not root :
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)

if __name__  == "__main__":
    arr = [25,20,50,40,10,30,25,50,0]
    avl = AVLTree()
    for el in arr :
        avl.insert(el)
        #avl.inorder()
    avl.inorder()
    for el in arr :
        avl.delete(el)
        avl.inorder()
