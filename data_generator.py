import random

def data_generator(size=10, max_value=100):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, max_value))
    return arr