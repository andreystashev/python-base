import simple_draw as sd

snowlist = []


def snow_num(x):
    snowlist.append(x)


snow_num(x=10)
# todo в этом модуле если в х подставлять значение, то оно передается в глобальную переменную, но если в 02 функцию
#  делать, то там значение ни на что не влияет. Не пойму, как сделать чтобы там можно было ввести число и оно передалось
#  сюда, и нужно ли это

N = snowlist[0]
x_point = [sd.random_number(10, 590) for _ in range(N)]
y_point = [sd.random_number(600, 700) for _ in range(N)]
length_list = [sd.random_number(10, 40) for _ in range(N)]


def snow_fall():
    for i in range(N):
        y_point[i] -= 40
        # if y_point[i] < -30:
        #     # y_point[i] += sd.random_number(600, 1000)
        #     for elem, value in enumerate(y_point):
        #         # if elem  <= -40:
        #         list_fall.append(elem)


snow_fall()


list_fall = []


def fall():
    for i in range(N):
        for elem, value in enumerate(y_point):
            if value < 0:
                list_fall.append(elem)
                break
            # print(elem, value)
            # print(list_fall)
# todo вот здесь у меня получается создается список который добавляет номера снежинок достигших низа. Но если посмотреть
#     что в нем, то там числа меняются на одинаковые

def snow_color(color):
    for i in range(N):
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=color)


def snow_del():
    for i in range(N):
        if i in list_fall:
            sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.background_color)
# todo А здесь пробовал использовать del, но выдается ошибка index out of range