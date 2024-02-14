# Домашнее задание по уроку Генерация функций.
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.

def create_operation(operation):
    if operation == "addition":
        def addition(x, y):
            return x + y

        return addition

    elif operation == "subtract":
        def subtract(x, y):
            return x - y

        return subtract

    elif operation == "multiplication":
        def multiplication(x, y):
            return x * y

        return multiplication

    elif operation == "division":
        def division(x, y):
            return x / y

        return division


my_func_add = create_operation("multiplication")
print(my_func_add(5, 2))

# result create_operation("multiplication") 10

# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат

multyply_squared = lambda x: x ** 2
result = multyply_squared(6)
print(f'result by lambda: {result}')

# result  by lambda 36

def squaring(x):
    return x ** 2


result = squaring(3)
print(f'result by def: {result}')


# result by def: 9

# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

    def __str__(self):
        return f'площадь прямоугольника {self.a} X {self.b} = {self.__call__()}'

square = Rect(4, 6)
result = square()
print(f'площадь прямоугольника = {result}')
# площадь прямоугольника = 24