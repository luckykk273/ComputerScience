from SortingAlgorithm.utils import create_array


def counting_sort(arr):
    # First find out the maximum and minimum elements in the unsorted array
    maximum = max(arr)
    minimum = min(arr)

    # Second count how many times each value i appears, and store it into the ith position of an auxiliary array
    auxiliary_arr = [0 for _ in range(maximum - minimum + 1)]
    for e in arr:
        auxiliary_arr[e-minimum] += 1

    # Third cumulate all count number
    # (Start from the first element in the auxiliary array)
    for i in range(1, len(auxiliary_arr)):
        auxiliary_arr[i] += auxiliary_arr[i-1]

    res = [0 for _ in range(len(arr))]
    for e in arr:
        res[auxiliary_arr[e-minimum] - 1] = e
        auxiliary_arr[e-minimum] -= 1

    return res


if __name__ == '__main__':
    unsorted_arr = create_array(100)
    print('Unsorted array:', unsorted_arr)
    sorted_arr = counting_sort(unsorted_arr)
    print('Sorted array:', sorted_arr)
