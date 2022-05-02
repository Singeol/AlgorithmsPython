def trapeze_integration(func, bottom_edge, top_edge, step_count):
    dx = (top_edge - bottom_edge) / step_count
    s = 0
    for i in range(step_count - 1):
        x = bottom_edge + dx * i
        s += (dx*(func((x + dx)) + func(x)) / 2)
    return s


def func(x):
    return x*x


print(trapeze_integration(func, -3, 3, 1000))
print(trapeze_integration(func, 0, 3, 100))
print(trapeze_integration(func, 0, 9, 1000))
print(trapeze_integration(func, 0, 9, 100))
