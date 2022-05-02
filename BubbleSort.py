def bubble_sorting(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                not_sorted = True
    return array


array = [-25, -26, 36, 69, 82, -19, 89, 88, -4, -2]
print(bubble_sorting(array))
array = [-13, 22, 72, 40, -37, 73, 66, -14, -26, 94]
print(bubble_sorting(array))
array = [-11, 24, -23, -12, -40, 96, 60, 49, 65, 26]
print(bubble_sorting(array))
array = [-6, 61, 25, 62, 42, -20, 80, -28, -24, -40]
print(bubble_sorting(array))
array = [8, 85, -31, 80, 43, 78, 42, 60, 46, 84]
print(bubble_sorting(array))
