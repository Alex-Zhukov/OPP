# Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_exception(Exception):
    def __init__(self):
        print('Деление на ноль!')

user_number = int(input())
user_divider = int(input())

try:
    if user_divider == 0:
        raise My_exception
except My_exception as err:
    print(err)