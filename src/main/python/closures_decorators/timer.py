import time


def timer(f):
    start = time.time()

    def wrapper(*args, **kwargs):
        ret_val = f(*args, **kwargs)
        end = time.time()

        print(f"function {f.__name__} took {end - start} to execute")
        return ret_val

    return wrapper


@timer
def foo(x, y):
    time.sleep(2)
    return x + y


print(foo(4, 5))
