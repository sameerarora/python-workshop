def find_pairs(numbers, target):
    visited = set()
    pairs = []
    for n in numbers:
        if (target - n) in visited:
            pairs += [(target - n, n)]
        else:
            visited.add(n)
    return pairs


if __name__ == '__main__':
    print(find_pairs([1, 3, 2, 4, 7, 9], 5))
