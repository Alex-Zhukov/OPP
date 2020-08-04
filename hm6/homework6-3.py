# Задание 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income["wage"]
        self._income_bonus = income["bonus"]


class Position(Worker):
    def get_full_name(self):
        return ('{} {}'.format(self.name, self.surname))

    def total_income(self):
        return (self._income_wage + self._income_bonus)


worker_1 = Position('Ivan', 'Ivanov', 'manager', {"wage": 1000, "bonus": 2000})
print(worker_1.get_full_name())
print(worker_1.total_income())
