"""Задача № 1. Подсчитать, сколько было выделено памяти под переменные в ранееразработанных программах в рамках первых
трех уроков. Проанализироватьрезультат и определить программы с наиболее эффективным использованием памяти.Примечание:
Для анализа возьмите любые 1-3 ваших программы или нескольковариантов кода для одной и той же здачи. Результаты анализа
вставьте в виде комментариев к коду. Также укажите в коментариях версию Python и разрядность вашей ОС."""

import sys


"""lesson_1 №1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

number = int(input('введите трёхзначное число: '))
mult = 1
sum = 0

for i in str(number):
    sum += int(i)
    mult *= int(i)

sum_member = sys.getsizeof(number) + sys.getsizeof(sum) + sys.getsizeof(mult)

print(f'сумма всех пременных - {sum_member}')
print(f'sum: {sum}, mult: {mult}')

"""lesson 2 №2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то
у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

number = int(input('введите число: '))
y = []
n = []
for i in str(number):
    if int(i) % 2 == 0:
        y.append(int(i))

    else:
        n.append(int(i))

sum_member = sys.getsizeof(number) + sys.getsizeof(y) + sys.getsizeof(n)

"""если i тоже считается за переменную, тогда эта переменная подойдёт:
sum_member = sys.getsizeof(number) + sys.getsizeof(y) + sys.getsizeof(n) + sys.getsizeof(i)"""

print(f'сумма всех пременных - {sum_member}')
print(f'чётные: {y}, нечётные: {n}')

"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
введено число 3486, то надо вывести число 6843."""

number = input('введите число: ')
number_reverse = int(number[::-1])

sum_member = sys.getsizeof(number) + sys.getsizeof(number_reverse)
print(f'сумма всех пременных - {sum_member}')
print(number_reverse)
