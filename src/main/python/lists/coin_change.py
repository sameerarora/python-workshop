def change(coins, amount):
    memo = [0] + [float('inf') for i in range(amount)]

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                memo[i] = min(memo[i], memo[i - c]) + 1
    if memo[-1] == float('inf'):
        return -1
    return memo[-1]


print(change([1, 2, 5], 5))
