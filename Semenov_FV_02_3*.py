'''

1.Вычислить и вывести на экран сумму кубов натуральных чисел
от 1 до n включительно. Верхний предел должен вводиться
с клавиатуры и не должен превышать числа 100.

'''

n = int(input("введите число: "))
for i in range(1,n+1):
    print(i**3)



'''

2.Выведите на экран таблицу умножения чисел от одного до девяти.

'''
print("таблица умножения")
for i in range(1,10):
    for q in range(1,10):
        print(f"{i*q:4}",end='')
    print()
