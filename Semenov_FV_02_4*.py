'''

Дана строка. Подсчитать самую длинную последовательность подряд
идущих букв «н». Преобразовать ее,
заменив точками все восклицательные знаки.

'''

string = input("введите строку: ")
s = ' '
a = []
c = 0
string = string + s
print(string)
for i in range(len(string)):
    if string[i] == 'н':
        c += 1
    else:
        a.append(c)
        c = 0
d = max(a)
print(d)
string = string.replace('!', '.')


'''

Дана строка символов, среди которых есть одна открывающаяся и
одна закрывающаяся скобки. Вывести на экран все символы,
расположенные внутри этих скобок.

'''

string = input("введите строку: ")
print(string[string.index('(') + 1:string.index(')')])


'''

Дана строка. Вывести все слова, начинающиеся на букву "а"
и слова оканчивающиеся на букву "я".

'''

string = input("введите строку: ")
string = string.lower()
for i in string.split():
    if i.startswith('а') or i.endswith('я'):
        print(i)
