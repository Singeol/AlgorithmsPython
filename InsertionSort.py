def insertion_sort(array):
    for i in range(len(array)):
        current = array[i]
        j = i - 1
        while ((j >= 0) and (array[j] > current)):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current
    return array


array = [-25, -26, 36, 69, 82, -19, 89, 88, -4, -2]
print(insertion_sort(array))
array = [-13, 22, 72, 40, -37, 73, 66, -14, -26, 94]
print(insertion_sort(array))
array = [-11, 24, -23, -12, -40, 96, 60, 49, 65, 26]
print(insertion_sort(array))
array = [-6, 61, 25, 62, 42, -20, 80, -28, -24, -40]
print(insertion_sort(array))
array = [8, 85, -31, 80, 43, 78, 42, 60, 46, 84]
print(insertion_sort(array))
