from SortingAlgorithm.utils import create_array


def counting_sort(arr, digit):
    length = len(arr)
    count = [0] * 10  # The same as the auxiliary array in `counting_sort.py`
    output = [0]*length

    # Count how many times each digit i(0-9) appears
    for i in range(length):
        # 723 // 1 % 10 = 723 % 10 = 3; 723 // 10 % 10 = 72 % 10 = 2;
        count[arr[i] // digit % 10] += 1

    # Accumulate all count number
    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(length-1, -1, -1):
        idx = arr[i] // digit % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1

    for i in range(length):
        arr[i] = output[i]


def radix_sort(arr):
    maximum = max(arr)
    digit = 1
    while digit < maximum:
        counting_sort(arr, digit)
        digit *= 10


if __name__ == '__main__':
    # arr = create_array(100)
    # # Here we only fulfill the non negative integer version, so we have to filter the negative number
    # arr = list(filter(lambda x: x > 0, arr))
    arr = [100, 45, 1]
    print('Unsorted array:', arr)
    radix_sort(arr)
    print('Sorted array:', arr)
