#Задание 1

class Date:

    def __init__(self, date_text):
        self.date_text = date_text

    @classmethod
    def numbers_from_date(cls, date_text):
        number_day, number_month, number_year = map(int, date_text.split('-'))
        return number_day, number_month, number_year

    @staticmethod
    def validation_date(date_text):
        number_day, number_month, number_year = map(int, date_text.split('-'))
        return number_day <= 31 and number_month <= 12 and number_year <= 9999


a = '17-12-2020'
if Date.validation_date(a):
    print(Date.numbers_from_date(a))
else:
    print('Неверные входные данные')

b = '13-13-2013'
if Date.validation_date(b):
    print(Date.numbers_from_date(b))
else:
    print('Неверные входные данные')

#Задание 2

class MyDivisionZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

divident = int(input('Введите число-делимое: '))
divider = int(input('Введите число-делитель: '))

try:
    if divider == 0:
        raise MyDivisionZeroError('Введите число, отличное от 0!')
except MyDivisionZeroError as err:
    print(err)
else:
    print(f'Результат деления: {divident / divider:.2f}')


#Задание 3

class OnlyIntError(Exception):

    def __init__(self, txt):
        self.txt = txt


my_number_list = []
el = None

while True:
    el = input('введите число ')
    if el == 'stop':
        break
    try:
        if not el.isdigit():
            raise OnlyIntError(f'{el} не число!')
        else:
            my_number_list.append(int(el))
    except OnlyIntError as err:
        print(err)

print(my_number_list)


#Задания 4 - 6

class OfficeEquipment():
    trade_mark = None

    def __init__(self, name):
        self.name = name


class Printers(OfficeEquipment):
    dpi = None


class Scanners(OfficeEquipment):
    speed = None


class Store:
    store_name = 'store_office_equipment'
    availability = {'pr_kyocera': 5, 'sc_samsung': 3}

    def arrival(self, nomenklature: OfficeEquipment, number):
        if nomenklature.name in self.availability.keys():
            self.availability[nomenklature.name] += number
        else:
            self.availability[nomenklature.name] = number
        return f'Наличие оргтехники на складе после прихода: {self.availability}'

    def consumption(self, nomenklature: OfficeEquipment, number, consumer):
        self.availability[nomenklature.name] -= number
        return f'Наличие оргтехники на складе после отгрузки в {consumer}: {self.availability}'

    #проверяю валидность номенклатуры и количества отгружаемой со склада техники
    def is_available(self, nomenklature: OfficeEquipment, number):
        if self.availability.get(nomenklature.name, -1) > number:
            return True


store1 = Store()
p1 = Printers('pr_kyocera')
s1 = Scanners('sc_kyocera')
print(store1.arrival(p1, 3))
print(store1.arrival(s1, 3))
print(store1.consumption(p1, 6, 'экономический отдел') if store1.is_available(p1, 6) else
      'Заявленной номенклатуры недостаточно или нет в наличии!')
print(store1.consumption(p1, 6, 'экономический отдел') if store1.is_available(p1, 6) else
      'Заявленной номенклатуры недостаточно или нет в наличии!')


# Задание 7

class ComplexNum:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
         return f'Комплексное число {self.re} + i*{self.im}'

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNum(self.re * other.re, self.im * other.im)


a = ComplexNum(5, 7)
b = ComplexNum(2, 4)
print(a + b)
print(a * b)
