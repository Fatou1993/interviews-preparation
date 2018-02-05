class TreeNode:
    def __init__(self, val=None, left=None, right=None, color="BLACK"):
        self.val = val
        self.left = left
        self.right = right
        self.color = color
        self.parent = None

    def printRoot(self):
        if self.left :
            self.left.printRoot()
        if self.val:
            print self.val, self.color
        if self.right:
            self.right.printRoot()

class RBTree :
    def __init__(self, root=None):
        self.root = root
        self.num_elements = 0
        self.RED = "RED"
        self.BLACK = "BLACK"
        self.NIL = TreeNode()

    def inorder(self):
        if not self.root :
            print ""
            return
        self.root.printRoot()
        print ""

    def lookUp(self, x):
        if not self.root :
            return None, None
        node = self.root
        parent = node.parent
        while node and node.val != x:
            parent = node
            node = node.right if node.val < x else node.left
        return node, parent

    def insert(self, x):
        node, parent = self.lookUp(x)
        if node:  # x already present
            return
        if not node and not parent :
            self.root = TreeNode(x)
            return
        node = TreeNode(x)
        if parent.val < x :
            parent.right = node
        else:
            parent.left = node
        node.parent = parent
        node.color = self.RED
        self.fixRBTreeInsert(node)

    def transplant(self, prev_node, new_node):
        parent = prev_node.parent
        if not parent : #element was root
            self.root = new_node
        else :
            if parent.left == prev_node :
                parent.left = new_node
            else:
                parent.right = new_node
        if new_node :
            new_node.parent = parent

    def findLeftMostElement(self, node):
        while node and node.left :
            node = node.left
        return node

    def delete(self, x):
        """
        Steps delete the node and find the node that replace it then fix the delete
        :param x:
        :return:
        """

        node, parent = self.lookUp(x)
        if not node : #x not present
            return
        #print node.val
        y = node
        y_original_color = y.color
        if not node.left :
            x = node.right
            self.transplant(node, node.right)
        elif not node.right :
            x = node.left
            self.transplant(node, node.left)
        else :
            y = self.findLeftMostElement(node.right)
            #print "replacement", y.val
            y_original_color = self.BLACK if not y else y.color
            x = y.right #element that will replace y
            if y.parent == node and x:
                x.parent = y
            else:
                self.transplant(y,y.right)
                y.right = node.right
                if node.right :
                    node.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            if node.left :
                node.left.parent = y
            y.color = node.color
        #self.inorder()
        if y_original_color == self.BLACK : #we replace new element by a black one so there are less black nodes on some path
            self.fixRBTreeDelete(x)

    def fixRBTreeDelete(self, node):
        #print(node.val if node else "")
        while node and node != self.root and node.color == self.BLACK :
            if node == node.parent.left :
                sibling = node.parent.right
                if sibling and sibling.color == self.RED :
                    sibling.color = self.BLACK
                    node.parent.color = self.RED
                    self.leftRotate(node.parent)
                    sibling = node.parent.right
                if not sibling or (not sibling.left and not sibling.right) or (sibling.left and sibling.left.color == self.BLACK and sibling.right and sibling.right.color == self.BLACK):
                    if sibling :
                        sibling.color = self.RED
                    node = node.parent
                elif not sibling.right or sibling.right.color == self.BLACK :
                    sibling.left.color = self.BLACK
                    sibling.color = self.RED
                    self.rightRotate(sibling)
                    sibling = node.parent.right
                #add one more black to path with sibling
                sibling.color = sibling.parent.color
                sibling.parent.color = self.BLACK
                if sibling.right :
                    sibling.right.color = self.BLACK
                self.leftRotate(node.parent)
                node = self.root
            else:
                sibling = node.parent.right
                if sibling and sibling.color == self.RED:
                    sibling.color = self.BLACK
                    node.parent.color = self.RED
                    self.rightRotate(node.parent)
                    sibling = node.parent.left
                if not sibling or (not sibling.right and not sibling.left) or (
                            sibling.left and sibling.left.color == self.BLACK and sibling.right and sibling.right.color == self.BLACK):
                    if sibling:
                        sibling.color = self.RED
                    node = node.parent
                elif not sibling.left or sibling.left.color == self.BLACK:
                    sibling.right.color = self.BLACK
                    sibling.color = self.RED
                    self.leftRotate(sibling)
                    sibling = node.parent.left
                    # add one more black to path with sibling
                sibling.color = sibling.parent.color
                sibling.parent.color = self.BLACK
                if sibling.left :
                    sibling.left.color = self.BLACK
                self.rightRotate(node.parent)
                node = self.root
        if node :
            node.color = self.BLACK


    def fixRBTreeInsert(self, node):
        while node.parent and node.parent.color == self.RED :
            if node.parent.parent.left == node.parent :
                uncle = node.parent.parent.right
                if uncle and uncle.color == self.RED :
                    uncle.color = self.BLACK
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right :
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    self.rightRotate(node.parent.parent)
                    return
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == self.RED:
                    uncle.color = self.BLACK
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotate(node.parent)
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    self.leftRotate(node.parent.parent)
                    return

        self.root.color = self.BLACK

    def leftRotate(self, node):
        node_parent = node.parent
        z = node.right
        node.right = z.left
        if z.left :
            z.left.parent = node
        if node_parent :
            if node_parent.left == node :
                node_parent.left = z
            else:
                node_parent.right = z
        else:
            self.root = z
        z.parent = node_parent
        z.left = node
        node.parent = z

    def rightRotate(self, node):
        node_parent = node.parent
        z = node.left
        node.left = z.right
        if z.right :
            z.right.parent = node
        if node_parent :
            if node_parent.left == node :
                node_parent.left = z
            else:
                node_parent.right = z
        else:
            self.root = z
        z.parent = node_parent
        z.right = node
        node.parent = z


if __name__ == "__main__":
    arr = [7,3,18,10,22,8,11,26]
    rbt = RBTree()
    for el in arr :
        rbt.insert(el)
        #rbt.inorder()
    for el in arr :
        print "Element deleted:", el
        rbt.delete(el)
        rbt.inorder()
''



