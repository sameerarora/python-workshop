def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    size_left, size_right = len(left), len(right)
    while left_idx < size_left and right_idx < size_right:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < size_left:
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < size_right:
        result.append(right[right_idx])
        right_idx += 1

    return result


if __name__ == '__main__':
    print(merge([4, 6, 7, 8], [2, 4, 7]))
