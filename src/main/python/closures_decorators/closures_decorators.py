def logging(f):
    print(f"Inside Logging")

    def foo(*args, **kwargs):
        print(f"Executing {f.__name__} with {args} and {kwargs}")
        return f(*args, **kwargs)

    return foo


@logging
def add(x, y):
    return x + y


add(4, 5)
# add_with_logging = logging(add)
# add_with_logging(4, 5)
