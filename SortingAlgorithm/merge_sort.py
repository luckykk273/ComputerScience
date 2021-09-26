from SortingAlgorithm.utils import create_array


def merge(arr, left_sub_arr, right_sub_arr):
    left_idx, right_idx, sorted_idx = 0, 0, 0
    # Find out the minimum element in both left and right sub-arrays:
    while left_idx < len(left_sub_arr) and right_idx < len(right_sub_arr):
        if left_sub_arr[left_idx] < right_sub_arr[right_idx]:
            arr[sorted_idx] = left_sub_arr[left_idx]
            left_idx += 1
        else:
            arr[sorted_idx] = right_sub_arr[right_idx]
            right_idx += 1

        sorted_idx += 1

    # After running out of elements either in left or right sub-array,
    # keep going through remaining elements in left and right sub-arrays:
    while left_idx < len(left_sub_arr):
        arr[sorted_idx] = left_sub_arr[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right_sub_arr):
        arr[sorted_idx] = right_sub_arr[right_idx]
        right_idx += 1
        sorted_idx += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_sub_arr = arr[:mid]
        right_sub_arr = arr[mid:]

        merge_sort(left_sub_arr)
        merge_sort(right_sub_arr)

        merge(arr, left_sub_arr, right_sub_arr)


if __name__ == '__main__':
    arr = create_array()
    print('Unsorted array:', arr)
    merge_sort(arr)
    print('Sorted array:', arr)
