def search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        left_num = numbers[start]
        right_num = numbers[end]
        mid = (end + start) // 2
        if target == numbers[mid]:
            return True
        else:
            if target > numbers[mid]:
                if target > right_num:
                    end = mid - 1
                elif target < right_num:
                    start = mid + 1
                else:
                    return True
            else:
                if target > left_num:
                    end = mid - 1
                else:
                    return not target < left_num

    return False


print(search([4, 5, 6, 7, 8, -2, -1, 0, 1, 2, 3], 100))
