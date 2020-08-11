# Задание 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex_numbers:
    def __init__(self, real_number, imag_number):
        self.number = complex(real_number, imag_number)
        print(self.number)

    def __add__(self, other):
        return (self.number + other.number)

    def __mul__(self, other):
        return self.number * other.number


z1 = Complex_numbers(1, 2)
z2 = Complex_numbers(2, 3)

print(z1 + z2)
print(z1 * z2)
