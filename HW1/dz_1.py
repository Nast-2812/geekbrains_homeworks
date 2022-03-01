#Задание 1

my_number = int(input('Введите любимое число: '))
print(my_number)

my_text = input('Напиши, что тебя сегодня порадовало: ')
print(my_text)

#Задание 2

my_time = int(input('Введите время в секундах: '))
time_h = my_time // 3600
time_min = (my_time % 3600) // 60
time_sec = my_time % 60

print(f'{time_h:02d}:{time_min:02d}:{time_sec:02d}')

#Задание 3

number = input('Введите число: ')
print(int(number * 3) + int(number * 2) + int(number))


#Задание 4
#Вариант 1 ( через while, как просили в задании)

my_num = input('Введите число: ')
i = 0
num_max = 0
while i < len(my_num):
    num_max = int(my_num[i]) if int(my_num[i]) >= num_max else num_max
    i += 1
print(num_max)

#Вариант 2
number_list = list(input('Введите число: '))
print(int(max(number_list)))

#Задание 5
procceds = int(input("Введите значение выручки за отчетный период: "))
costs = int(input("Введите значение издержек за отчетный период: "))

profit = procceds - costs
if profit > 0:
    print(f'Ваша прибыль составила: {profit} руб.')
    print(f'Рентабельность составила: {(profit / procceds * 100):.2f} %')
    workers = int(input('Введите кол-во сотрудников организации: '))
    print(f'Прибыль в расчете на одного сотрудника составила: {profit / workers} руб.')
elif profit < 0:
    print(f'Ваш убыток составил: {profit} руб.')
else:
    print('Вы работали, чтобы работать ((( ...')

#Задание 6
a = int(input('Введите результат 1-го дня: '))
b = int(input('Введите цель: '))
day = 1

while a < b:
    day += 1
    a = a * 1.1
    print(f'день {day} - {a:.2f} км')
print(day)
