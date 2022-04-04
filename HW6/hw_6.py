#Задание 1
import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'yellow'
        print(self.__color)
        time.sleep(2)
        self.__color = 'green'
        print(self.__color)
        time.sleep(4)
        return


a = TrafficLight()
a.running()



#Задание 2
class Road:
    def __init__(self, lengt, width):
       self.lengt = lengt
       self.width = width

    def mass_asphalt(self, mass_sqv_meter, thickness):
        self.mass_sqv_meter = mass_sqv_meter
        self.thickness = thickness
        return self.lengt * self.width * mass_sqv_meter * thickness


print(Road(1, 2).mass_asphalt(25, 5))



#Задание 3
class Worker:
    name = 'Sergey'
    surname = 'Ivanov'
    position = 'engineer'
    _income = {'wage': 50000, 'bonus': 1000}


class Position(Worker):
    def get_full_name(self):
        return f'Имя, фамилия сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


b = Position()
b.name = 'Kate'
b.surname = 'Smoleva'
b.position = 'economist'
b._income = {'wage': 77000, 'bonus': 1000}

print(b.get_full_name())
print(b.get_total_income())



#Задание 4
class Car:
    speed = 50
    color = 'red'
    name = 'Nissan'
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Направление движения - {self.direction}')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def town_car_method(self):
        print('Это метод из дочернего класса TownCar')

    def show_speed(self):
        print('Вы превысили скорость!' if self.speed > 60 else self.speed)


class SportCar(Car):
    def sport_car_method(self):
        print('Это метод из дочернего класса SportCar')


class WorkCar(Car):
    def work_car_method(self):
        print('Это метод из дочернего класса WorkCar')

    def show_speed(self):
        print('Вы превысили скорость!' if self.speed > 40 else self.speed)


class PoliceCar(Car):
    def police_car_method(self):
        print('Это метод из дочернего класса PoliceCar')


a= Car()
a.speed = 150
a.color = 'белый'
a.name = 'Audi'
a.is_police = False
print(f'Скорость движения {a.speed} км/ч')
print(f'Цвет автомобиля {a.color}')
print(f'Марка автомобиля {a.name}')
print(f'Принадлежность к полиции: {a.is_police}')
a.go()
a.stop()
a.turn('направо')
a.show_speed()

b = TownCar()
b.speed = 100
b.color = 'серый'
b.name = 'Lada'
b.is_police = False
b.town_car_method()
b.go()
b.stop()
b.turn('налево')
b.show_speed()

c = SportCar()
c.speed = 200
c.color = 'черный'
c.name = 'Ferrari'
c.is_police = False
c.sport_car_method()
c.go()
c.stop()
c.turn('прямо')
c.show_speed()

d = WorkCar()
d.speed = 41
d.color = 'желтый'
d.name = 'Cat'
d.is_police = False
d.work_car_method()
d.go()
d.stop()
d.turn('прямо')
d.show_speed()

e = PoliceCar()
e.speed = 60
e.color = 'зеленый'
e.name = 'Нива'
e.is_police = True
e.police_car_method()
e.go()
e.stop()
e.turn('назад')
e.show_speed()



#Задание 5
class Stationery:
    title = 'ruler'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Запуск подписи документа')


class Pensil(Stationery):

    def draw(self):
        print('Запуск построения чертежа')


class Handle(Stationery):

    def draw(self):
        print('Запуск выделения наиболее важных мест')


a = Stationery()
a.draw()

b = Pen()
b.draw()

c = Pensil()
c.draw()

d = Handle()
d.draw()
