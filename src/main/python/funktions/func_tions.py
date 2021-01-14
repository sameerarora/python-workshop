def foo(*args, **kwargs):
    print(f"received {len(args)} arguments")
    print(f"received {len(kwargs)} keyword arguments")
    print(f"packed {kwargs} ")
    print(f"packed {args} ")
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(f"{k}:{v}")


foo(1, "sameer", 2, "age", person_name="John", age=25)
# kwargs -> keyworkd argumnets
#
# def higher_order_function(a):
#     print(f"function name is  {a.__name__}")
#     return a(7, 4)  # square(7) => 49
#
#
# def square(x, y):
#     return x ** y
#
#
# def cube(x, y):
#     return x ** y
#
#
# print(higher_order_function(square))
# print(higher_order_function(cube))
#
# print(higher_order_function(lambda x, y: x ** y))
