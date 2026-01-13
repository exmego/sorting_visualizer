
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):

            yield array.copy(), j, j+1 # 交换前

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

            yield array.copy(), j, j+1 # 交换后