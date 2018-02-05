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

def reconstruct_from_plain_level_order(nodes):
    n  = len(arr)
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

if __name__ == "__main__":
    arr = [3,9,20,None,None,15,7]
    root = reconstruct_from_plain_level_order(arr)
    root.printRoot()


