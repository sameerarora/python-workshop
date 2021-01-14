class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, next):
        self.next = next

    def __eq__(self, other):
        return self.value == other.value
