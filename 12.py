def divide_numbers(a, b):

    try:
        return (a / b)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        return "Ошибка: аргументы должны быть числами."
print(divide_numbers(10, 'b'))