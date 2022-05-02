def binary_search(value, array):
    left = 0
    right = len(array)
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        if value > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


array = [-30, -14, 11, 17, 39, 45, 48, 57, 68, 84]
print(binary_search(17, array))
array = [-35, -31, -27, -14, 3, 52, 73, 74, 76, 91]
print(binary_search(-35, array))
array = [-30, -13, -11, 0, 5, 39, 45, 53, 94, 95]
print(binary_search(95, array))
array = [-41, -23, -8, 18, 19, 20, 26, 34, 53, 65]
print(binary_search(-8, array))
array = [-48, -39, -16, -12, 30, 36, 45, 55, 85, 90]
print(binary_search(30, array))
array = [-23, -9, -5, 2, 6, 31, 72, 87, 88, 97]
print(binary_search(72, array))
array = [-47, -25, -4, -3, 0, 6, 19, 38, 74, 92]
print(binary_search(0, array))
array = [-32, 27, 30, 32, 39, 43, 61, 63, 78, 91]
print(binary_search(45, array))
array = [-30, -28, -22, -14, -4, 5, 12, 18, 77, 78]
print(binary_search(0, array))
array = [-11, 23, 31, 40, 57, 80, 85, 86, 91, 96]
print(binary_search(50, array))
