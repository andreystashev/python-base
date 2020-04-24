import simple_draw as sd

N = 10
x_point = [sd.random_number(10, 590) for _ in range(N)]
y_point = [sd.random_number(600, 900) for _ in range(N)]
length_list = [sd.random_number(10, 40) for _ in range(N)]


def snow_fall():
    for i in range(N):
        y_point[i] -= 30


def snow_color(color):
    for i in range(N):
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=color)


def get_fallen():
    global res
    res = []
    for i, value in enumerate(y_point):
        if value < 0:
            res.append(i)

    return res


def snow_del():
    res.reverse()
    for i in res:
        del x_point[i]
        del y_point[i]
        del length_list[i]


def return_snow():
    res.reverse()
    x = sd.random_number(10, 590)
    y = sd.random_number(600, 900)
    z = sd.random_number(10, 40)
    for _ in res:
        x_point.append(x)
        y_point.append(y)
        length_list.append(z)
