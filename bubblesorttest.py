import random


def bubble_sort(array):
    array_accesses = 0
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            array_accesses += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break
    return array, array_accesses

for list_size in [5, 10, 25, 50, 75, 100, 125, 250, 500]:
    total_array_accesses = []
    for i in range(100):
        numbers = list(range(list_size))
        random.shuffle(numbers)
        sorted, array_accesses = bubble_sort(numbers)
        total_array_accesses.append(array_accesses)
    average_accesses = sum(total_array_accesses) / len(total_array_accesses)
    print('List size:', list_size, '- Average accesses:', average_accesses)

