'''квадртное уравнение'''

import math

a = float(input("введите a \n"))
b = float(input("введиете b \n"))
c = float(input(" введите с \n"))
d = b**2 - 4 * a * c
if (d > 0):
    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
    print("корни квадратного уровнения: ", x1, " ", x2)
if (d == 0):
    x = -b / 2 * a
    print("корень квадратного уровнения; ", x)
else:
    print("квадратное уровнение корней не имеет")


'''

1. Написать программу, которая будет делить введенные пользователем
два вещественных числа и выводить результат на экран,
сообщая об ошибке в случае деления на ноль.

'''
divisible = float(input("введите делимое \n"))
divider = float(input("введите делитель \n"))
if divider == 0:
    print("ошибкка деления на ноль")
else:
    print("частное равно: ", divisible / divider)


'''

2. Рассчитать стоимость покупки с учетом скидки в 35%,
которая предоставляется покупателю, если сумма покупки превышает 20 у.е.
Сумму покупки ввести с клавиатуры, а результаты округлить
до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость
и размер предоставленной скидки.

'''

cost = float(input("введте стоимость покупки \n"))
if cost > 20:
    discount = round((0.35 * a), 2)
    cost = cost - discount
    print("стоимость покупки составляет: ", cost, "у.е")
    print("стоимость скидки составляет: ", discount, "у.е")
else:
    print("стоимость покупки составляет: ", cost, "у.е")


'''

3. Напишите скрипт, который по введенному пользователем числу от 1 до 12,
будет выводить на экран сообщение в виде названия месяца и времени года.
Если пользователь введет недопустимое число,
программа должна выдавать сообщение об ошибке.

'''

month = int(input("введите номер месяца \n"))
if month == 1:
    print("январь-зима")
if month == 2:
    print("февраль-зима")
if month == 3:
    print("март-весна")
if month == 4:
    print("апрель-весна")
if month == 5:
    print("май-весна")
if month == 6:
    print("июнь-лето")
if month == 7:
    print("июль-лето")
if month == 8:
    print("август-лето")
if month == 9:
    print("сентябрь-осень")
if month == 10:
    print("октябрь-осень")
if month == 11:
    print("ноябрь-осень")
if month == 12:
    print("декабрь-зима")
