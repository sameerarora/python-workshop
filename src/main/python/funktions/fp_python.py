from functools import reduce

numbers = [1, 3, 2, -1, -4, 21, 6]

print(sorted(numbers, key=lambda x: x ** 2))

fruits = ['pineapple', 'apple', 'guava', 'fig', 'banana']  # ananab gif

print(sorted(fruits, key=lambda x: x[::-1]))

print(sum([n ** 2 for n in numbers]))
print(reduce(lambda x, y: x * y, [1, 2, 4]))


def calculator(o, *args):
    o(args)
