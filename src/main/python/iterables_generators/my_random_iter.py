from random import choice, shuffle, randint

class RandomIterator():
    def __init__(self, l):
        self.data = l

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) == 0:
            raise StopIteration
        v = choice(self.data)
        self.data.remove(v)
        return v


r_itr = RandomIterator([1, 2, 3, 4, 5])

for element in r_itr:
    print(element, end=" ")
