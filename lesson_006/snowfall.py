import simple_draw as sd


def snow_num(x):
    print()


N = 10
x_point = [sd.random_number(10, 590) for _ in range(N)]
y_point = [sd.random_number(0, 0) for _ in range(N)]
length_list = [sd.random_number(10, 40) for _ in range(N)]


def snow_fall():
    for i in range(N):
        y_point[i] -= 40
        if y_point[i] < -30:
            y_point[i] += sd.random_number(600, 1000)


def snow_color(color):
    for i in range(N):
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=color)
