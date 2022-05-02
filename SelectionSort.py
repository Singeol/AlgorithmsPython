def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        minId = i
        for j in range(i+1, len(array)):
            if array[j] < min:
                min = array[j]
                minId = j
        array[minId] = array[i]
        array[i] = min
    return array


array = [-25, -26, 36, 69, 82, -19, 89, 88, -4, -2]
print(selection_sort(array))
array = [-13, 22, 72, 40, -37, 73, 66, -14, -26, 94]
print(selection_sort(array))
array = [-11, 24, -23, -12, -40, 96, 60, 49, 65, 26]
print(selection_sort(array))
array = [-6, 61, 25, 62, 42, -20, 80, -28, -24, -40]
print(selection_sort(array))
array = [8, 85, -31, 80, 43, 78, 42, 60, 46, 84]
print(selection_sort(array))
