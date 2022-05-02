def draw_symbol_plot(calculator, bottom_edge, top_edge, string_count):
    dx = (top_edge - bottom_edge) / string_count
    ordinates = [int(calculator(bottom_edge + i * dx)) for i in range(string_count + 1)]
    origin = min(ordinates)
    for ordinate in ordinates:
        print(' ' * (ordinate - origin) + '*')


def func(x):
    return x*x*x


draw_symbol_plot(func, -3.5, 3.5, 20)
