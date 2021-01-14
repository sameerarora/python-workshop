from lists.stack import Stack
from lists.node import Node


def is_balanced(word):
    s = Stack()
    for c in word:
        if c == '(':
            s.push(Node(c))
        elif c == ')':
            if s.head is not None:
                s.pop()
            else:
                return False
    return s.head is None


print(is_balanced('(()))'))
print(is_balanced('()()((()))'))
