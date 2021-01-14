numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print([n ** 2 for n in numbers if n % 2 == 0])

#Args and Kwargs

def foo(*args, **kwargs):
    for arg in args:
        print(arg)
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k}:{v}")


# foo(1, "name", True, name='Sameer', age=30)

dictionary = {'name': 'Sameer', 'age': 30}
l = ["Some_value", True, 45, 1.0]
foo(*l, **dictionary)
