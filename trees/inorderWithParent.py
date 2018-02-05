def inorder(root):
    if not root :
        return []
    res = []
    parent = root.parent
    while parent or root :
        if root :
            parent = root
            root = root.left
        else:
            root = parent
            res.append(root.data)
            root = root.right
            while parent.parent and parent.parent.right == parent :
                parent = parent.parent
    return res