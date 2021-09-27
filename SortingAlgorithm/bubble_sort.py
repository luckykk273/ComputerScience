from SortingAlgorithm.utils import create_array


def swap(arr: list, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr):
    length = len(arr)
    count = 0
    for i in range(length-1):  # Control the number of operations: n elements need to iterate n-1 times
        for j in range(length-i-1):  # After every time we operate, we will get one more largest element at the last, so we can compare one less time
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
        count += 1


if __name__ == '__main__':
    arr = create_array()
    print('Unsorted array:', arr)
    bubble_sort(arr)
    print('Sorted array:', arr)
