from random import randint


# Create randomized, unsorted arrays
def create_array(size=10, max_=100):
    return [randint(0, max_) for _ in range(size)]


# This is the simplest(in my opinion) implementation but is with extra storing memory
def quick_sort(arr: list):
    length = len(arr)

    if length <= 1:
        return arr

    smaller, equal, larger = [], [], []  # Using another memory here
    pivot = arr[randint(0, length-1)]  # Pick up a randomized value be the pivot to avoid worst case

    for e in arr:
        if e < pivot:
            smaller.append(e)
        elif e > pivot:
            larger.append(e)
        else:
            equal.append(e)

    return quick_sort(smaller) + equal + quick_sort(larger)


def partition(arr: list, front: int, end: int):
    i = front  # Looks for an element that is bigger than the pivot element
    j = end - 1  # Looks for an element that is smaller than the pivot element
    pivot = arr[end]

    while i < j:
        while i < end and arr[i] < pivot:
            i += 1
        while j > front and arr[j] >= pivot:
            j -= 1

        # If i, j don't meet(cross), it means that:
        # i finds an element is bigger than the pivot and j finds an element is smaller than the pivot;
        # So just swap them;
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:  # If i and j crossed:
        arr[i], arr[end] = arr[end], arr[i]

    return i


def quick_sort_in_place(arr: list, front: int, end: int):
    if front < end:
        partition_pos = partition(arr, front, end)  # First find out the partition position

        # Recursively call the quick sort function for the left and right sub-array
        quick_sort_in_place(arr, front, partition_pos-1)
        quick_sort_in_place(arr, partition_pos+1, end)


if __name__ == '__main__':
    print('Not in-place: ')
    unsorted_arr = create_array()
    print('Unsorted array:', unsorted_arr)
    sorted_arr = quick_sort(unsorted_arr)
    print('Sorted array:', sorted_arr)
    print('============================')
    print('In-place: ')
    arr = create_array()
    print('Unsorted array:', arr)
    quick_sort_in_place(arr, 0, len(arr) - 1)
    print('Sorted array:', arr)
