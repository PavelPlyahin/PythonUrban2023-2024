#Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c='True'):
    print(a, b, c)
print_params()

print_params(1, 2)
print_params(1, 2,3)
print_params(b= 25)
print_params(c= [1,2,3])

# Распаковка параметров:
values_list = [1, 'два', 3]
values_dict = {'a': 1, 'b': 'два', 'c': 3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'три']
print_params(*values_list_2, 42)





