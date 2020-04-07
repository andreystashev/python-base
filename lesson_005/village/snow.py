import simple_draw as sd


def snow():

    n = 10

    x_point = [sd.random_number(-50, 200) for _ in range(n)]
    y_point = [sd.random_number(0, 0) for _ in range(n)]
    length_list = [sd.random_number(10, 30) for _ in range(n)]

    sd.circle(center_position=sd.get_point(50, 600), color=sd.COLOR_RED, radius=90, width=89)

    while True:

        for i in range(n):

            sd.start_drawing()
            sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.background_color)
            y_point[i] -= 30
            x_point[i] += sd.random_number(-20, 20)
            sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.COLOR_WHITE)
            sd.finish_drawing()

            if y_point[i] < 50:
                y_point[i] += sd.random_number(300, 450)
                sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.COLOR_WHITE)
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


if __name__ == '__main__':
    snow()
