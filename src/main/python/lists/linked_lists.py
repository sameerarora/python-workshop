from lists.node import Node


def reverse(head, k, root=None):
    a, result = None, None
    while head is not None:
        for i in range(0, k):
            if head is None:
                break
            root = Node(head.value, root)
            head = head.next
        if a is None:
            result = Node(root.value, root.next)
            a = result
        else:
            while a.next is not None:
                a = a.next
            a.next = Node(root.value, root.next)
        root = None
    return result


n1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))

r = reverse(n1, 5)

while r is not None:
    print(r.value, end=' ')
    r = r.next
# 2 1 4 3 6 5
