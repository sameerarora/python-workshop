from lists.node import Node


class Stack:

    def __init__(self, head=None):
        self.head = head

    def push(self, elem: Node):
        if self.head is None:
            self.head = elem
        else:
            elem.set_next(self.head)
            self.head = elem

    def pop(self):
        elem = self.head
        if self.head is not None:
            self.head = elem.next
            return elem.value


if __name__ == '__main__':
    s = Stack()
    s.push(Node(1))
    s.push(Node(2))
    s.push(Node(3))

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
