def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # 比较
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr.copy(), i, min_idx, j

        # 交换
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr.copy(), i, min_idx, -1
