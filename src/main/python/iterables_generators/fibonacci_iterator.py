# Iterables and Iterators
class Fibonacci():

    def __init__(self, upper_bound):
        self.curr, self.prev = 1, 0
        self.upper_bound = upper_bound

    def __iter__(self):
        return self

    def __next__(self):
        self.curr, self.prev = self.curr + self.prev, self.curr
        if self.curr > self.upper_bound:
            raise StopIteration
        return self.curr


for n in Fibonacci(100):
    print(n, end=' ')
print("done!!")

i = iter(Fibonacci(1000))
try:
    while True:
        n = next(i)
        print(n, end=" ")
except StopIteration:
    print("done!!")
