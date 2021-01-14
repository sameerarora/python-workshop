class Fibonacci():
    # init iter next __ __
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.prev, self.curr = self.curr, self.curr + self.prev
        if self.curr > 1000:
            raise StopIteration
        return self.curr


fibo = Fibonacci()
itr = iter(fibo)
try:
    while True:
        n = next(itr)
        print(n, " ")
except StopIteration:
    print("Done!!")
