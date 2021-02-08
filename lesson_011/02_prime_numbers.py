# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
from operator import eq


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         self.prime_numbers = []
#         self.i = 2
#         return self
#
#     def __next__(self):
#         for number in range(self.i, self.n + 1):
#             for prime in self.prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 self.i = number
#                 self.prime_numbers.append(number)
#                 return number
#         raise StopIteration


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if not number % prime:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def get_palindrome_digits(n):
    return True if str(n)[::-1] == str(n) else False


# for number in prime_numbers_generator(n=10000):
#     print(number, get_palindrome_digits(number), sep=' ')


def get_lucky_digits(number_):
    number_ = str(number_)
    middle = len(number_) // 2
    return True if sum(map(int, number_[:middle])) == sum(map(int, number_[-middle:])) else False


# for prime_number in prime_numbers_generator(n=10000):
#     print(prime_number, get_lucky_digits(prime_number), sep=' ')


def prime_numbers_generator(n, func):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if not number % prime:
                break
        else:
            prime_numbers.append(number)
            if func(number):
                yield number, True
            else:
                yield number, False


def get_mersenne_numbers(digit):
    return (digit + 1) & digit == 0


for value, mersenne_check in prime_numbers_generator(n=10000, func=get_mersenne_numbers):
    print(value, mersenne_check)


# зачет!
