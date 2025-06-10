'''''''''
def task_1() -> None:
    # Создаем переменные с произвольными названиями и соответствующими типами
    age: int = 25
    temperature: float = 36.6
    name: str = "Маша"
    numbers: list = [1, 2, 3, 4, 5]
    is_active: bool = True

    # Выводим тип данных каждой переменной
    print(type(age))
    print(type(temperature))
    print(type(name))
    print(type(numbers))
    print(type(is_active))

# Вызов функции
task_1()
'''''''''''

'''''''''
def task_2() -> None:
    a: list[int] = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3]) #Такая последовательность чисел называется - последовательность Фибоначчи

# Вызов функции
task_2()
'''''''''''

'''''''''
def task_3() -> None:
    a: int = 12
    """
    Возвращает квадрат переданного числа.
    """
    return a**2

#Вызов функции
print(task_3())
'''''