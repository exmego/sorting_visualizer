def insert_sort(arr):
    n = len(arr)


    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            yield arr.copy(), j, j+1
            j -= 1

        arr[j + 1] = key

        yield arr.copy(), j+1, i
