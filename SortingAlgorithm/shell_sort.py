from SortingAlgorithm.utils import create_array


def shell_sort(arr):
    length = len(arr)
    gap = length // 2  # There are lots of rules to determine the gap; Here we use the original rule: N/2, N/4, ..., 1
    while gap > 0:
        for i in range(gap, length):  # Iterate from gap to the last element
            temp = arr[i]
            j = i
            while j >= gap and temp < arr[j-gap]:  # Compare with the element at the same position in every split array
                arr[j], arr[j-gap] = arr[j-gap], arr[j]
                j -= gap

            arr[j] = temp

        gap //= 2


if __name__ == '__main__':
    arr = create_array(99)
    print('Unsorted array:', arr)
    shell_sort(arr)
    print('Sorted array:', arr)
