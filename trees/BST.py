import random

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self):
        if self.left :
            self.left.inorder()
        if self.val != None:
            print self.val,
        if self.right:
            self.right.inorder()

class BST :
    def __init__(self, root=None):
        self.root = root
        self.num_elements = 0

    def inorder(self):
        self.root.inorder()
        print ""

    def insert(self, x):
        """
        Insert x in BST and no duplicate allowed
        :param x:
        :return:
        """
        if not self.root :
            self.root = TreeNode(x)
            return
        parent = None
        node = self.root
        while node :
            if node.val == x : #duplicate
                return
            parent = node
            if node.val < x :
                node = node.right
            else:
                node = node.left
        self.num_elements+=1
        if x < parent.val :
            parent.left = TreeNode(x)
        else:
            parent.right = TreeNode(x)
        return

    def transplant(self, prev_node, new_node, prev_node_parent):
        if not prev_node_parent : #the node was root
            self.root = new_node
        else:
            if prev_node_parent.left == prev_node:
                prev_node_parent.left = new_node
            else :
                prev_node_parent.right = new_node

    def findLeftMostAndItsParent(self, node, parent) :
        while node and node.left :
            parent = node
            node = node.left
        return node, parent

    def delete(self, x):
        if not self.root :
            return
        parent = None
        node = self.root
        while node and node.val != x:
            parent = node
            if node.val < x :
                node = node.right
            else:
                node = node.left
        if not node :
            return #element not present
        self.num_elements -= 1
        if not node.left :
            return self.transplant(node, node.right, parent)
        elif not node.right :
            return self.transplant(node, node.left, parent)
        else:
            y, y_parent = self.findLeftMostAndItsParent(node.right, node) #find the leftmost element in the right of node and its parent
            if y_parent != node :
                self.transplant(y, y.right, y_parent)  # replace y by its right
                y.right = node.right  # put y at the right of node
            self.transplant(node, y, parent)  # replace node by y
            y.left = node.left

        return



def generate_random_integers(n):
    arr = list(range(n))
    for i in range(n-1):
        r = random.randint(i,n-1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr


if __name__ == "__main__":
    bst = BST()
    arr = generate_random_integers(20)
    #arr = [3, 4, 1, 5, 0, 2]
    for x in arr :
        bst.insert(x)
        #bst.inorder()
    print arr
    bst.delete(5)
    bst.inorder()
    #print bst.root.right.val
