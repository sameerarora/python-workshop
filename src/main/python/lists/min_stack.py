from lists.stack import Stack
from lists.node import Node


class MinStack():

    def __init__(self):
        self.items = Stack()
        self.mins = Stack()

    def push(self, elem: Node):
        self.items.push(elem)
        if self.mins.head is None or elem.value < self.mins.head.value:
            self.mins.push(Node(elem.value))
        else:
            self.mins.push(Node(self.mins.head.value))

    def pop(self):
        self.mins.pop()
        return self.items.pop()

    def min(self):
        return self.mins.head.value


ms=MinStack()

ms.push(Node(2))
print(ms.min())
ms.push(Node(3))
print(ms.min())
ms.push(Node(1))
print(ms.min())
ms.pop()

print(ms.min())
ms.pop()
print(ms.min())


