# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).

import types


def introspection_info(obj):
    info = {}
    module = obj.__class__.__module__
    class_name = obj.__class__.__name__
    attributes = obj.__dict__.keys()
    methods = dir(obj)

    info['Type'] = class_name
    info['Module'] = module
    info['Attributes'] = attributes
    info['Methods'] = methods

    return info

number_info = introspection_info(42)
print(number_info)
