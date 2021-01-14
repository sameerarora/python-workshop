def find_pairs(arr, target):
    low, high = 0, len(arr) - 1
    pairs = []
    while high >= low:
        if arr[low] + arr[high] > target:
            high = high - 1
        elif arr[low] + arr[high] < target:
            low = low + 1
        else:
            pairs.append((arr[low], arr[high]))
            low, high = low + 1, high - 1
    return pairs


print(find_pairs([-1, -1, 0, 1, 2, 3, 4, 5, 6, 9], 2))
