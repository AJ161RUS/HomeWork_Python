# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазон(5,15)
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

List1 =[randint(-10, 25) for i in range(10)]
print(List1)
res = []
min_num = int(input('Введите минимальное значение: '))
max_num = int(input('Введите максимальное значение: '))
for i in range (len(List1)):
    if min_num <= List1[i] <= max_num:
        res.append(i)
print(res)