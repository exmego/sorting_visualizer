from data_generator import data_generator
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from visualizer import visualize
from algorithms.insert_sort import insert_sort
from algorithms.selection_sort import selection_sort

data = data_generator(50)

gen1 = bubble_sort(data.copy())
gen2 = insert_sort(data.copy())
gen3 = quick_sort(data.copy(), 0, len(data) - 1)
gen4 = selection_sort(data.copy())

visualize(gen1, gen2, gen3, gen4, data)