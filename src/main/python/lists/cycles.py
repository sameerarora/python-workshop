from lists.node import Node

five = Node(5)
four = Node(4, five)
three = Node(3, four)
two = Node(2, three)
head = Node(1, two)


# five.set_next(head)


def kth_last_node(head, k):
    first = head
    second = head
    for i in range(k):
        second = second.next
    while second is not None:
        second = second.next
        first = first.next
    return first.value


def has_cycle(head: Node):
    first = head
    second = head.next

    while first is not None and second is not None:
        if first == second:
            return True
        else:
            first, second = first.next, second.next.next
    return False


if __name__ == '__main__':
    print(has_cycle(head))
    print(kth_last_node(head, 3))
