from math import log2, ceil
import random
from time import sleep

test_num = random.randint(1, 100)


def min_iter(n):  # Поиск мин. кол-ва гарантированных итераций
    global min_it
    for i in range(1, int(n) + 1):
        num1 = log2(i)
        min_it = ceil(num1)
    return min_it


def is_valid(num):  # "Защита от дурака"
    return num.isdigit() and 1 <= int(num) <= 100 and not None


print('Здравствуйте и добро пожаловать в числовую угадайку!')
sleep(2)
print('Коротко о правилах: компьютер загадал число, '
      'Вам нужно его отгадать за минимальное количество ходов')
sleep(1)


while True:
    sleep(2)
    print('Пожалуйста, введите число от 1 до 100')
    num = input()
    if is_valid(num) is False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if is_valid(num) is True:
        print('Хорошо, начнём))')
    break

while True:
    if int(num) < test_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        num = input()
    elif int(num) > test_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        num = input()
    elif int(num) == test_num:
        print('Вы угадали, поздравляем!')
        sleep(3)
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
sleep(5)
