# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

N = int(input('Колличество монет: '))
o = 0
r = 0

for n in range (N):
    m = int(input('Укажите сторону сторону (1 - орел) и (0 - решка): '))
    if m == 1:
        o == 1
        o += 1
    else:
        r += 1
if (o > r):
    print("переверните монеты с решки на орла: ")
elif (o == r):
    print("равное количество монет орла и решки")
else:
    print("переверните с орла на решку")


