def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if j % 2 == 0:
            yield arr.copy(), i, j

    # pivot 放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr.copy(), i + 1, high

    pi = i + 1
    # 递归左右
    yield from quick_sort(arr, low, pi - 1)
    yield from quick_sort(arr, pi + 1, high)
