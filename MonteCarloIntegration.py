from random import random


def monte_carlo_integration(func, bottom_edge, top_edge, point_count):
    y_min = float('inf')
    y_max = float('-inf')
    i = bottom_edge
    while i <= top_edge:
        f = func(i)
        y_min = min(y_min, f)
        y_max = max(y_max, f)
        i += 1
    under_curve = 0
    for i in range(point_count):
        x = bottom_edge + random() * (top_edge - bottom_edge)
        f = y_min + random() * (y_max - y_min)
        if f <= y_min + func(x):
            under_curve += 1
    return (top_edge - bottom_edge) * (y_max - y_min) * under_curve / point_count


print(monte_carlo_integration(lambda x: x, -5, 5, 100000))
print(monte_carlo_integration(lambda x: x**3, 0, 9, 1000000))
print(monte_carlo_integration(lambda x: x**2, -3.0, 3.0, 10000))
print(monte_carlo_integration(lambda x: x**2, 0, 9.0, 10000))
