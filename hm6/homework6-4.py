# Задание 4.  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула :', direction)

    def show_speed(self):
        print('Скорость', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Скорость', self.speed)
        if self.speed > 60:
            print('Превышение скорости !')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Скорость', self.speed)
        if self.speed > 40:
            print('Превышение скорости !')


class PoliceCar(Car):
    pass


# police = PoliceCar(70, 'blue', 'police', True)
# police.show_speed()


town_car = TownCar(120,'Yellow', 'town_car', False)
town_car.go()
town_car.turn('right')
town_car.show_speed()