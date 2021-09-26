from SortingAlgorithm.utils import create_array


def insertion_sort(arr):
    for i in range(1, len(arr)):
        boundary = arr[i]

        j = i-1
        while j > -1 and arr[j] > boundary:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = boundary


if __name__ == '__main__':
    arr = create_array()
    print('Unsorted array:', arr)
    insertion_sort(arr)
    print('Sorted array:', arr)
