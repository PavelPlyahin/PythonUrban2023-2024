# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
class IntrospectionHelper:
    def __init__(self, obj):
        self.obj = obj

    def get_type(self):
        return type(self.obj)

    def get_attributes(self):
        return dir(self.obj)

    def get_methods(self):
        methods = []
        for attr in self.get_attributes():
            if attr[0] != '_' and callable(getattr(self.obj, attr)):
                methods.append(attr)
        return methods

    def get_module(self):
        module = self.obj.__class__.__module__
        if module == 'builtins':
            module = 'None'
        return module

def introspection_info(obj):
    helper = IntrospectionHelper(obj)
    info = {
        'type': helper.get_type(),
        'attributes': helper.get_attributes(),
        'methods': helper.get_methods(),
        'module': helper.get_module()
    }
    return info


number_info = introspection_info('Привет буфет 1984 ')
print(number_info)
