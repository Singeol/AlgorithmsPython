def adaptive_integration(integration, func, bottom_edge, top_edge, accuracy):
    temp = 0
    step_count = 2
    square = integration(func, bottom_edge, top_edge, step_count)
    while abs(temp - square) > accuracy:
        step_count *= 2
        temp = square
        square = integration(func, bottom_edge, top_edge, step_count)
    return square


def rectangle_integration(func, bottom_edge, top_edge, step_count):
    dx = (top_edge - bottom_edge) / step_count
    s = 0
    for i in range(step_count):
        x = bottom_edge + dx * i
        s += dx * func(x)
    return s


def func(x):
    return x*x


print(adaptive_integration(rectangle_integration, func, -10, 10, 0.0001))
print(adaptive_integration(rectangle_integration, func, -100, 100, 0.0001))
print(adaptive_integration(rectangle_integration, func, -3.1, 4.7, 0.001))
print(adaptive_integration(rectangle_integration, func, -3.1, 4.7, 0.00001))
