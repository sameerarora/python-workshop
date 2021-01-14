def fibonacci_gen():
    prev, curr = 0, 1
    while True:
        yield curr
        curr, prev = curr + prev, curr


generator = fibonacci_gen()
for i in range(20):
    n = next(generator)
    print(n, end=' ')
