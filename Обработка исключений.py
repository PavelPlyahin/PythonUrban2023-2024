def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}' в целое число."
print(string_to_int('s'))  # Ошибка: невозможно преобразовать 's' в целое число.
print(string_to_int('4'))  # 4

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{file_name}' не найден."
    except IOError:
        return f"Ошибка вывода/вывода при работе с файлом '{file_name}'."
    except UnicodeError:
        return 'UnicodeError:'
print(read_file('Text.txt')) # печать текста из файла
print(read_file('Test.txt')) # Ошибка: файл 'Test.txt' не найден.

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except TypeError:
        return "Ошибка: аргументы должны быть числами."
print(divide_numbers(10, 0))   # Ошибка: деление на ноль.
print(divide_numbers(10, 5))   # 2.0
print(divide_numbers('f', 5))  # Ошибка: аргументы должны быть числами.

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} вне диапозона списка."
    except TypeError:
        return "Ошибка: индекс должен быть целым числом."
print(access_list_element([1, 2, 3], 1))  # 2
print(access_list_element([1, 2, 3], 4))  # Ошибка: индекс 4 вне диапозона списка.
print(access_list_element(3, 3))          # Ошибка: индекс должен быть целым числом.