def merge_sort(arr):

    if len(arr) <= 1:
        yield arr.copy(), -1, -1
        return

    # 创建可变的工作数组
    work_arr = arr[:]
    aux = work_arr[:]

    def _merge_sort_range(low, high):
        if high - low <= 1:
            return
        mid = (low + high) // 2
        yield from _merge_sort_range(low, mid)
        yield from _merge_sort_range(mid, high)

        # 复制到 aux
        for i in range(low, high):
            aux[i] = work_arr[i]

        i, j, k = low, mid, low
        while i < mid and j < high:
            if aux[i] <= aux[j]:
                work_arr[k] = aux[i]
                i += 1
            else:
                work_arr[k] = aux[j]
                j += 1
            k += 1

        while i < mid:
            work_arr[k] = aux[i]
            i += 1
            k += 1

        # 合并完成后，yield 当前完整状态
        yield work_arr.copy(), k, k

    # 开始递归
    yield from _merge_sort_range(0, len(work_arr))
    # 最终状态（确保完整）
    yield work_arr.copy(), -1, -1