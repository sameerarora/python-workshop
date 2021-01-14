def error_handler(f):
    def handle(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ZeroDivisionError as divide_by_zero_error:
            print(f"you are playing a dangerous game here: {divide_by_zero_error}")
            return 0
        except TypeError:
            print("There was a type error not returing a value")

    return handle




@error_handler
def foo(x, y):
    return x / y


print(foo(4, 5))
print(foo(4, 0))
print(foo(4))
