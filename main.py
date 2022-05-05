def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        return merge(arr, left, right)


def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    else:
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quicksort(arr, left, pivot)
    quicksort(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[left]
    leftWall = left

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            leftWall += 1
            arr[i], arr[leftWall] = arr[leftWall], arr[i]

    arr[left], arr[leftWall] = arr[leftWall], arr[left]

    return leftWall


def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(merge_sort([4, 6, 1, 4, 7, 3, 9, 0, -1]))
    print(quicksort([4, 6, 1, 4, 7, 3, 9, 0, -1], 0, 8))
    print(QuickSort([4, 6, 1, 4, 7, 3, 9, 0, -1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
