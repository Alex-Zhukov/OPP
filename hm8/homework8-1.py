# Задание 1. 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def classmet(cls, date):
        sep_date = []
        for el in date.split('-'):
            sep_date.append(el)

        print(int(sep_date[0]), int(sep_date[1]), int(sep_date[2]))

    @staticmethod
    def staticmet(day, month, year):
        if 1 <= day <= 31:
            print(month, end=' ')
        else:
            print('Неверное число')

        if 1 <= month <= 12:
            print(month, end=' ')
        else:
            print('Неверный месяц')

        if 1 <= year <= 2050:
            print(year, end=' ')
        else:
            print('Неверный год')


Date.classmet('27-10-2019')
print()
Date.staticmet(32, 15, 2019)
