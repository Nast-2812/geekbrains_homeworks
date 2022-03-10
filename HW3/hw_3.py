#Задание 1

def division1(a, b):
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        print('Деление на 0!')
    return division


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
print(division1(a, b))


#Задание 2

def data_user (name, surname, year_birth, residance, email, tel):
    return (f'{name} {surname}, {year_birth} г.р., проживает в {residance}, email: {email}, тел.: {tel}')


data_alex = data_user (name='Александра' , surname='Усеня', year_birth=1977, residance='г.Минск', email='au@mail.ru', tel='+375291234567')
print(data_alex)


#Задание 3

#Var1
def sum_2(a, b, c):
    return sum(sorted([a, b, c])[1:])


#Var2
def sum_2_var2(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


print(sum_2(10, 1, 1000))
print(sum_2_var2(10, 1, 1000))


#Задание 4

def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    z = 1
    for i in range(abs(y)):
        z = z * x
    return 1 / z


print(my_func1(3, -5))
print(my_func2(3, -5))


#Задание 5

def my_sum():
    sum = 0
    while True:
        line_numbers = input('Введите строку из чисел: ').split()
        try:
            for i in line_numbers:
                sum += int(i)
        except ValueError:
            print(sum)
            break
        print(sum)


my_sum()


#Задание 6

def int_func(word):
    return word.title()


print (int_func('line'))


#Задание 7

print(' '.join(map(int_func, input('Введите строку: ').split())))
