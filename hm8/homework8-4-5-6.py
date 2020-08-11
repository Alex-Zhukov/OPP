# Задание 4.

class Stock:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.dict = {}

    def reception(self, name, amount):
        try:
            if amount <= self.capacity:
                self.capacity -= amount
                self.dict[name] = amount
                print(f'Товар принят, свободного места - {self.capacity}')
            else:
                print('Склад заполнен')
        except:
            print('Введите количество в числах')

    def shipment(self, name, amount, destination='main_office'):
        try:
            if amount <= self.dict[name]:
                self.capacity += amount
                self.dict[name] = self.dict[name] - amount
                print(f'Товар отправлен в {destination}, свободное место - {self.capacity}')
            else:
                print('Недостаточно товара')
        except:
            print('Введите количество в числах')


class Office_equip:
    def __init__(self, name):
        self.name = name


class Printer(Office_equip):
    def printing(self, number):
        print('printing {} lists'.format(number))


class Scaner(Office_equip):
    def scanning(self, number):
        print('scanning {} lists'.format(number))


class Copier(Office_equip):
    def copying(self, number):
        print('copy {} lists'.format(number))


stock = Stock('Moscow', 500)
stock.reception('printers', 200)
stock.reception('scanners', 'dw')
stock.shipment('printers', 112)
stock.reception('xerox', 300)

cuorsera = Printer('fx2000')
cuorsera.printing(20)
print(stock.dict)
