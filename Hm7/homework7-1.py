# Задание 1.  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        result = ''
        for row in self.matr:
            for el_in_row in row:
                result += ' ' + str(el_in_row)
            result += '\n'
        return result

    def __add__(self, other):
        sum_result = ''
        if len(self.matr) == len(other.matr):
            for row1, row2 in zip(self.matr, other.matr):
                if len(row1) != len(row2):
                    return ("Длины строк не равны")
                for el_row1, el_row2 in zip(row1, row2):
                    sum_result += ' ' + str(el_row1 + el_row2)
                sum_result += '\n'
        else:
            return ("Длины столбовцов не равны")
        return sum_result


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
