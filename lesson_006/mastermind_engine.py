import simple_draw as sd

final_number = []


def random_number():
    while True:
        num1 = sd.random_number(1, 9)
        num2 = sd.random_number(0, 9)
        num3 = sd.random_number(0, 9)
        num4 = sd.random_number(0, 9)

        random1 = {num1, num2, num3, num4}
        if len(random1) == 4:
            random = num1, num2, num3, num4
            final_number.extend(random)
            break
    # print(int(random[0]), int(random[1]), int(random[2]), int(random[3]))


random_number()

win = []


def find():
    value_input = input("Введите четырехзначное число: ")

    if len(set(value_input)) == 4:
        cow = 0
        bull = 0

        for i in range(4):
            if int(value_input[i]) == (final_number[i]):
                bull += 1
            elif int(value_input[i]) in final_number:
                cow += 1

        print('>  быки - ', bull, ', коровы - ', cow)
        if bull == 4:
            print('you win')
            win.append('w')
            del final_number[0:4]
            random_number()

    elif len(set(value_input)) != 4:
        print('не верный ввод')

