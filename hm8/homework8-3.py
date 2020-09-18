# Задание 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class My_Exception(Exception):
    def __init__(self):
        print('Введите число')


user_list = []
user_word = True
while user_word:
    user_word = input()
    if user_word == 'stop':
        user_word = False
    else:
        try:
            if user_word.isdigit() == False:
                raise My_Exception
        except My_Exception as err:
            print(err)
        else:
            user_list.append(user_word)

print(user_list)
