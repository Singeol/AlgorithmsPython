def linear_search(value, array):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


array = [30, 33, 46, 8, 64, 36, 18, 87, 25, 10]
print(linear_search(64, array))
array = [18, 4, 28, 10, 83, 66, 77, 77, 63, 36]
print(linear_search(10, array))
array = [2, 8, 75, 36, 4, 77, 67, -70, 86, 73]
print(linear_search(37, array))
array = [20, 27, 26, 61, 27, 55, 88, 25, 89, 14]
print(linear_search(25, array))
array = [13, 76, 13, 0, 33, 37, 14, 23, 30, 84]
print(linear_search(73, array))
array = [33, 37, 59, 19, -9, 79, 87, 11, 67, 83]
print(linear_search(64, array))
array = [41, 29, 69, 83, 59, 11, 9, 4, 84, 67]
print(linear_search(4, array))
array = [74, 51, 67, 0, 82, -59, 17, 27, 28, 64]
print(linear_search(0, array))
array = [62, 45, 29, 3, 29, 25, 26, 44, 37, 85]
print(linear_search(44, array))
array = [3, -28, 18, 81, 74, 78, 43, 20, 43, 21]
print(linear_search(78, array))
