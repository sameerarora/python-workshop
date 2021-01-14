def merge(intervals):
    result = [intervals[0]]
    counter = 1
    res_idx = 0

    while counter < len(intervals):
        left, right = result[res_idx], intervals[counter]
        if left[1] >= right[0]:
            result[res_idx] = (left[0], max(left[1], right[1]))
        else:
            result.append(right)
            res_idx += 1
        counter += 1
    return result


print(merge([(1, 2), (3, 5), (4, 6)]))
print(merge([(1, 7), (4, 5), (4, 9)]))
