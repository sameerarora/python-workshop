from lists.node import Node


class Queue:
    def __init__(self):
        self.head, self.tail = None, None

    def add(self, elem: Node):
        if self.head is None:
            self.head, self.tail = elem, elem
        else:
            self.tail.next, self.tail = elem, elem

    def remove(self):
        if self.head is not None:
            e, self.head = self.head, self.head.next
            return e.value


q = Queue()
q.add(Node(1))
q.add(Node(2))
q.add(Node(3))
q.add(Node(4))

print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
