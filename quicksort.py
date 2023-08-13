# Quick sort

def quicksort(array):
    size = len(array)
    assert not size == 0, 'Non-empty list expected , got size=0'
    _quicksort(array, 0, size - 1)


def _quicksort(array, low, high):
    if low < high:
        pi = _partition(array, low, high)

        _quicksort(array, low, pi - 1)
        _quicksort(array, pi + 1, high)


def _partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1
