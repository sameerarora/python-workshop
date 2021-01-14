def common_prefix(words):
    prefix = ''
    index = 0
    while True:
        l = []
        for w in words:
            l.append(w[index])
        if len(set(l)) == 1:
            prefix += l[0]
            index += 1
        else:
            return prefix


print(f'Result is {repr(common_prefix(["platypus", "plank", "plant"]))}')
print("Result is " + repr(common_prefix(['dog', 'cat', 'parrot'])))
