def binary_search(arr, target):
    mid = (0 + len(arr)) // 2
    if len(arr) == 0:
        return False
    if target > arr[mid]:
        return binary_search(arr[mid + 1:], target)
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    elif arr[mid] == target:
        return True


print(binary_search(list(range(10)), 7))
