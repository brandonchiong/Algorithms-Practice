def partition(array, left, right):
    pivot = array[int((left + right) / 2)]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return left

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot = partition(array, start, end)
    quicksort(array, start, pivot - 1)
    quicksort(array, pivot, end)

example = [8, 3, 6, 1, 2, 7, 9, 5, 4]
quicksort(example)
print(example)

example2 = [245, 92, 3, 42, 875, 54, 128, 999, 17, 88]
quicksort(example2)
print(example2)
