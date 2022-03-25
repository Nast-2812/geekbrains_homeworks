# Задание 1

from sys import argv

def pay(t, a, b):
    return t * a + b



if len(argv) == 1:
    time_h = input('Введите время выработки, ч: ')
    rate_h = input('Введите часовую ставку, руб.: ')
    bonus = input('Введите размер бонуса, руб.: ')
else:
    time_h, rate_h, bonus = argv[1:]

print(pay(int(time_h), int(rate_h), int(bonus)))


# Задание 2

list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 125, 125]
new_list = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i - 1]]
print(new_list)


# Задание 3

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])


# Задание 4

list_2 = [2, 2, 2, 7, 23, 11, 231, 44, 44, 3, 2, 10, 7, 4, 11]
list_unique = [i for i in list_2 if list_2.count(i) == 1]
print(list_unique)


# Задание 5

from functools import reduce

def mltplc(a, b):
    return a * b


list_3 = range(100, 1001, 2)

print(reduce(mltplc, list_3))

# Задание 6

from itertools import count, cycle

for i in count(7, 7):
    if i > 100:
        break
    else:
        print(i)

counter = 0
for j in cycle(['Cogito', 'Ergo', 'Sum']):
    if counter > 8:
        break
    print(j)


    counter += 1


#Задание 7

def fact(n):
    el = 1
    for i in range(1, n + 1):
        el = el * i
        yield el


for el in fact(7):
    print(el)
