if True:
    x = 'global x'  # x will persist outside this block

print("outside the block, x =", x)


def func():
    x = 'func x'  # declare var inside function
    print("x =", x)
    d = locals()
    print(d)
    print("local x =", d['x'])
    d = globals()
    print(d)
    print("global x =", d['x'])


func()
