from random import randint


# Create randomized, unsorted arrays
def create_array(size=10, max_=100):
    return [randint(0, max_) for _ in range(size)]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]

        j = i-1
        while j > -1 and arr[j] > pivot:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = pivot


if __name__ == '__main__':
    arr = create_array()
    print('Unsorted array:', arr)
    insertion_sort(arr)
    print('Sorted array:', arr)
