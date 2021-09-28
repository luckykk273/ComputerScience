from SortingAlgorithm.utils import create_array


def heapify(arr, size, idx):
    largest = idx
    left, right = 2 * idx + 1, 2 * idx + 2

    if left < size and arr[left] > arr[largest]:  # If left isn't out of range and is larger than the root
        largest = left

    if right < size and arr[right] > arr[largest]:  # If right isn't out of range and is larger than the root
        largest = right

    if largest != idx:  # If the root is not the largest, swap it
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr, size, largest)


def heap_sort(arr):
    """
    Given a node at index i and suppose we start from i = 0:
        1. Its left child is at index 2 * i + 1
        2. Its right child is at index 2* i + 2
        3. Its parent child is at index i//2

    Max heap: In every sub-tree, the root value is greater its two children values
        - value(i) > value(2i) and value(i) > value(2i+1)
    Min heap: In every sub-tree, the root value is smaller its two children values
        - value(i) < value(2i) and value(i) < value(2i+1)

    """
    size = len(arr)

    # First build the max heap
    for i in range(size//2, -1, -1):
        heapify(arr, size, i)

    # After heapifying as before, we get a max heap(root is the largest)
    for i in range(size-1, 0, -1):
        # Swap the root(the largest) and the last node(element in the array),
        # so now the last node is the largest;
        arr[i], arr[0] = arr[0], arr[i]

        # Then we heapify the array except the last i elements
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = create_array(100)
    print('Unsorted array:', arr)
    heap_sort(arr)
    print('Sorted array:', arr)
