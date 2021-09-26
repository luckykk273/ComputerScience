from SortingAlgorithm.utils import create_array


def selection_sort(arr):
    for i in range(len(arr)):  # Traversal all elements in array
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = create_array()
    print('Unsorted array:', arr)
    selection_sort(arr)
    print('Sorted array:', arr)