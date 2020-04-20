import simple_draw as sd

N = 20
x_point = [sd.random_number(10, 590) for _ in range(N)]
y_point = [sd.random_number(600, 700) for _ in range(N)]
length_list = [sd.random_number(10, 40) for _ in range(N)]


def snow_fall():
    for i in range(N):
        y_point[i] -= 40

def snow_color(color):
    for i in range(N):
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=color)

def get_fallen():
    res = []
    for i, value in enumerate(y_point):
        if value < 0:
            res.append(i)
    return res

def snow_del(indexes):
    pass
    # TODO здесь нужно обойти индексы в обратном порядке и удалить элементы из всех списков

# TODO не хвататет еще функции которая добавляла бы новые снежинки взамен упавших
#  для бесконечного снегопада