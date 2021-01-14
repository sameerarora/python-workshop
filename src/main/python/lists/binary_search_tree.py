class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_depth(root, depth=0):
    if root is None:
        return depth
    else:
        return 1 + max(max_depth(root.left, depth), max_depth(root.right, depth))


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=' ')
    inorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=' ')


def preorder(root):
    if root is None:
        return
    print(root.value, end=' ')
    preorder(root.left)
    preorder(root.right)


def insert(root, value):
    if root.value > value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)

if __name__ == '__main__':
    root = Node(1)

    insert(root, 4)
    insert(root, 3)
    insert(root, 7)
    insert(root, -2)
    insert(root, 2)
    insert(root, 9)

    print(max_depth(root))
