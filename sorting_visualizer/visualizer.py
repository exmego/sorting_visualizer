import copy
import matplotlib
matplotlib.use("TkAgg")
from itertools import zip_longest
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualize(generator1, generator2, generator3, generator4, data):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    bars1 = ax1.bar(range(len(data)), data)
    bars2 = ax2.bar(range(len(data)), data)
    bars3 = ax3.bar(range(len(data)), data)
    bars4 = ax4.bar(range(len(data)), data)

    ax1.set_ylim(0, max(data)*1.1)
    ax2.set_ylim(0, max(data)*1.1)
    ax3.set_ylim(0, max(data) * 1.1)
    ax4.set_ylim(0, max(data) * 1.1)

    ax1.set_title('Bubble Sort')
    ax2.set_title('Insertion Sort')
    ax3.set_title('Quick Sort')
    ax4.set_title('Selection Sort')

    final1 = copy.deepcopy(data)
    final2 = copy.deepcopy(data)
    final3 = copy.deepcopy(data)
    final4 = copy.deepcopy(data)

    def update(frame):
        f1, f2, f3, f4 = frame

        if f1 is None:
            array1, i1, j1 = final1, -1, -1
        else:
            array1, i1, j1 = f1
            final1[:] = array1

        if f2 is None:
            array2, i2, j2 = final2, -1, -1
        else:
            array2, i2, j2 = f2
            final2[:] = array2

        if f3 is None:
            array3 = final3
        else:
            array3, _, _ = f3
            final3[:] = array3

        if f4 is None:
            array4, i4, min4, j4 = final4, -1, -1, -1
        else:
            array4, i4, min4, j4 = f4
            final4[:] = array4

        for idx, bar in enumerate(bars1):
            bar.set_height(array1[idx])
            bar.set_color("red" if idx == i1 or idx == j1 else "blue")


        for idx, bar in enumerate(bars2):
            bar.set_height(array2[idx])
            bar.set_color("red" if idx == i2 or idx == j2 else "blue")


        for idx, bar in enumerate(bars3):
            bar.set_height(array3[idx])
            bar.set_color("blue")

        for idx, bar in enumerate(bars4):
            if idx == i4:
                bar.set_color("green")  # 已确定位置
            elif idx == min4:
                bar.set_color("red")  # 当前最小
            elif idx == j4:
                bar.set_color("orange")  # 正在比较
            else:
                bar.set_color("blue")
            bar.set_height(array4[idx])

    anim = FuncAnimation(fig, update, frames=zip_longest(generator1,generator2,generator3,generator4), interval=10,
                         cache_frame_data=False, repeat = False )
    plt.show()