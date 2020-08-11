# Задание 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return (self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return self.number - other.number
        else:
            return 'Разность количества клеток меньше или равно 0'

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number // other.number

    def make_order(self, inrow):
        result = ''
        for i in range(1, self.number + 1):
            if i % inrow != 0:
                result += '*'
            else:
                result += '*\n'
        return result


cell_1 = Cell(42)
cell_2 = Cell(17)
print(cell_1.make_order(17))
print(cell_1 / cell_2)
