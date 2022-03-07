#Задание 1
my_list1 = [7, 'Надежда', True, 9.8]
for elem in my_list1:
    print(type(elem))

#Задание 2
n = int(input('Введите кол-во элементов в списке: '))
my_list2 = []

for el in range(n):
    my_list2.append(input('Введите что-нибудь: '))

n = n if n % 2 == 0 else (n - 1)
for i in range(0, n, 2):
    my_list2[i], my_list2[i + 1] = my_list2[i + 1], my_list2[i]

print(my_list2)

#Задание 3
list1 = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень',  'зима']
dict1 = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
month = int(input('Введите № месяца: '))
print(f'Это {list1[month - 1]}')

for key, value in dict1.items():
    if month in value:
        print(f'Это {key}')

#Задание 4
my_line = input('Введите строку: ')
for ind, el in enumerate(my_line.split(), 1):
    print(ind, el[:10])

#Задание 5
rating = [9, 6, 6, 5, 5, 3]

new_rat = int(input('Введите новый элемент рейтинга: '))
i = 0
for el in rating:
    if new_rat <= el:
        i += 1
    else:
        break
rating.insert(i, new_rat)
print(rating)

n = int(input())
rating = [i for i in rating if i >= n] + [n] + [i for i in rating if i < n]
print(rating)

#Задание 6
spis = []
n = int(input('Введите кол-во товаров: '))

for i in range(n):
    spis.append((i + 1,
    {"название": input('Введите название товара: '),
    "цена": int(input('Введите цену: ')),
    "кол-во": int(input('Введите кол-во: ')),
    "ед": input('Введите единицу измерения: ')}))
print(spis)

analiz_products = dict.fromkeys(spis[0][1].keys())
for element in spis:
    for key, value in element[1].items():
        if analiz_products[key] is None:
            analiz_products[key] = []
        analiz_products[key].append(value)

print(analiz_products)
