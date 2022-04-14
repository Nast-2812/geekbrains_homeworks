# Задание 1

with open ('text1.txt', 'w', encoding='utf-8') as f:
    line = None
    while line != '\n':
        line = input('Введите что-нибудь: ') + '\n'
        f.write(line)


# Задание 2

qvnt_words = []
with open('text2.txt', 'r', encoding='utf-8') as text:
    for line in text:
        qvnt_words.append(len(line.split()))

print(f'Количество строк в тексте - {len(qvnt_words)}')
for ind, el in enumerate(qvnt_words, 1):
    print(f'Количество слов в строке {ind} - {el}')


# Задание 3

from statistics import mean

sheet_pay = {}
with open ('text3.txt', 'r', encoding='utf-8') as f_pay:
     for line in f_pay:
         sheet_pay[line.split()[0]] = int(line.split()[1])

pays = sheet_pay.values()
print(f'Средняя величина дохода сотрудника {mean(pays):.2f} руб.')

print('Список сотрудников с доходом меньше 20000 руб.:')
for key, value in sheet_pay.items():
    if value < 20000:
        print(key)


# Задание 4

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
new_text = ''
with open('text4.txt', 'r', encoding='utf-8') as my_numbers:
    for line in my_numbers:
        first_word = line.split()[0]
        new_text += line.replace(first_word, my_dict[first_word])

with open('text4_1.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)


# Задание 5

with open('text5.txt', 'w', encoding='utf-8') as f_numbers:
    n = input('Введите строку из чисел через пробел: ')
    f_numbers.write(n)

print(sum(map(int, n.split())))

# Задание 6

import re

my_subjects = {}
with open('text6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        my_subjects[line.split(': ')[0]] = sum(map(int, re.findall(r'\d+', line)))

print(my_subjects)

# Задание 7

import json

from statistics import mean

results = [{}]
with open('text7.txt', 'r', encoding='utf-8') as list_firms:
    for line in list_firms:
        name, i, proceeds, costs = line.split()
        results[0][name] = int(proceeds) - int(costs)

results.append({'average_profit': mean(filter(lambda i: i > 0, results[0].values()))})
print(results)

with open('text7_1.json', 'w') as f_json:
    json.dump(results, f_json)

