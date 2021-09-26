from SortingAlgorithm.insertion_sort import insertion_sort
from SortingAlgorithm.utils import create_array


def bucket_sort(arr, num_of_buckets):
    # Count the range between each bin
    range_ = (max(arr) - min(arr)) / num_of_buckets

    # Create buckets
    buckets = [[] for _ in range(num_of_buckets)]

    # Scatter: put every element into corresponding bucket
    minimum = min(arr)
    for e in arr:
        idx = int((e-minimum)/range_) - 1 if int((e-minimum)/range_) >= num_of_buckets else int((e-minimum)/range_)
        buckets[idx].append(e)

    # Inner sort: sort the elements in every bucket(usually use the insertion sort)
    for bucket in buckets:
        if bucket:
            insertion_sort(bucket)

    # Gather: gather all elements in every sorted bucket
    i = 0
    for bucket in buckets:
        if bucket:
            for e in bucket:
                arr[i] = e
                i += 1


if __name__ == '__main__':
    arr = create_array(100)
    print('Unsorted array:', arr)
    bucket_sort(arr, 10)
    print('Sorted array:', arr)
