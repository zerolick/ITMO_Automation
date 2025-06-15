'''''''''
class Rectangle:
    def __init__(self, length, width): # length - длина, width - ширина
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(10, 5)
print("1 прямоугольник")
print("Площадь:", rect1.area())
print("Периметр:", rect1.perimeter())
rect2 = Rectangle(30, 13)
print("2 прямоугольник")
print("Площадь:", rect2.area())
print("Периметр:", rect2.perimeter())
rect3 = Rectangle(4, 12)
print("3 прямоугольник")
print("Площадь:", rect3.area())
print("Периметр:", rect3.perimeter())

------------------------------------------------------

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Делить на 0 нельзя"

add = Math(6, 2)
sub = Math(4, 10)
mul = Math(3, 13)
div = Math(35, 80)
print("Результат сложения:", add.addition())
print("Результат вычитания:", sub.subtraction())
print("Результат умножения:", mul.multiplication())
print("Результат деления:", div.division())
'''

# Доп. задание №4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска автомобиля установлен на {self.year}")

    def set_type(self, type):
        self.type = type
        print(f"Тип автомобиля установлен на {self.type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля установлен на {self.color}")

# Пример использования
if __name__ == "__main__":
    my_car = Car("Красный", "седан", 2020)
    my_car.start()
    my_car.set_year(2025)
    my_car.set_type("хэтчбек")
    my_car.set_color("синий")
    my_car.stop()









































































