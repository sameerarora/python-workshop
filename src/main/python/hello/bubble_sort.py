# [0,1,2,3,4,6,7,8] 4 [4,6,7,8] 2

def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_num = arr[i]
        while i > 0 and arr[i - 1] > curr_num:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = curr_num
    return arr


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


print(insertion_sort([9, 5, -2, 0, 6]))
