import time


def timer(f):
    def inner(*args, **kwargs):
        start = time.time()
        ret_val = f(*args, **kwargs)
        end = time.time()
        print(f"function {f.__name__} took {end - start} seconds to execute!!")
        return ret_val

    return inner



@timer
def baz(x, y):
    time.sleep(0.2)
    return x ** y


@timer
def foo():
    time.sleep(1)
    print("foo is done!!!!")


@timer
def bar():
    time.sleep(1)
    print("bar is done!!!!")


print(foo())
bar()
print(baz(4, 5))
