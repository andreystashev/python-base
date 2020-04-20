import simple_draw as sd

list1 = []


def random_number():
    while True:
        num1 = sd.random_number(1, 9)
        num2 = sd.random_number(0, 9)
        num3 = sd.random_number(0, 9)
        num4 = sd.random_number(0, 9)

        random1 = {num1, num2, num3, num4}
        if len(random1) == 4:
            random = num1, num2, num3, num4
            list1.extend(random)
            break
    print(int(random[0]), int(random[1]), int(random[2]), int(random[3]))


random_number()


def find():
    value_input = input("Введите четырехзначное число: ")
    random_input = {value_input[0], value_input[1], value_input[2], value_input[3]}    # TODO почему название random_input?
    # TODO множество можно сразу сделать из строки - она итерируемый объект

    if len(random_input) == 4:
        cow = 0
        bull = 0
        for i in range(4):
            if int(value_input[i]) == (list1[i]):
                bull += 1
            elif int(value_input[i]) in list1:
                cow += 1

        print('>  быки - ', bull, ', коровы - ', cow)
    else:
        print('not')
    if bull == 4:
        print('you win')
