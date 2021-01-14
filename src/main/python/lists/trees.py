class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth(node: Node):
    if node is None:
        return 0
    else:
        return 1 + max(depth(node.left), depth(node.right))


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, ' ')
    inorder(root.right)


two = Node(2, Node(3), Node(4))
root = Node(1, two, Node(6))
print(depth(root))

two = Node(2, right=Node(3, right=Node(4)))
root = Node(1, two, Node(6))
print(inorder(root))
